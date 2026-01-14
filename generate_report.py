
import pandas as pd
import base64
import os

# Paths
REPORT_PATH = "report.html"
DATA_DIR = "data/processed"

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    return ""

def generate_html():
    # Load data
    try:
        df_rfm = pd.read_csv(f"{DATA_DIR}/cluster_rfm_summary.csv")
        df_rules = pd.read_csv(f"{DATA_DIR}/cluster_top_rules.csv")
        df_compare = pd.read_csv(f"{DATA_DIR}/systematic_comparison.csv")
        df_model = pd.read_csv(f"{DATA_DIR}/model_comparison.csv")
        pca_base64 = get_base64_image(f"{DATA_DIR}/cluster_pca.png")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Personas
    personas = {
        0: {
            "name": "Occasional Shoppers - Khách hàng vãng lai",
            "desc": "Khách hàng mua sắm không thường xuyên, giá trị đơn hàng trung bình thấp.",
            "strategy": "Gửi email re-engagement, tặng mã giảm giá cho đơn hàng tiếp theo để tăng tần suất quay lại."
        },
        1: {
            "name": "Loyal Decorators - Tín đồ trang trí thân thiết",
            "desc": "Khách hàng mua sắm thường xuyên, chi tiêu cao, đặc biệt quan tâm đến các bộ sản phẩm trang trí.",
            "strategy": "Chương trình khách hàng thân thiết (VIP), ưu đãi mua theo combo (Bundle Scandi decoration), giới thiệu sớm các bộ sưu tập mới."
        }
    }

    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Customer Segmentation Report</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            :root {{
                --primary: #2563eb;
                --secondary: #64748b;
                --bg: #f8fafc;
                --card: #ffffff;
                --text: #1e293b;
            }}
            body {{
                font-family: 'Inter', sans-serif;
                background-color: var(--bg);
                color: var(--text);
                line-height: 1.6;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 1000px;
                margin: 40px auto;
                padding: 0 20px;
            }}
            header {{
                text-align: center;
                margin-bottom: 50px;
            }}
            h1 {{ font-size: 2.5rem; margin-bottom: 10px; color: var(--primary); }}
            .card {{
                background: var(--card);
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
                margin-bottom: 30px;
            }}
            h2 {{ border-left: 5px solid var(--primary); padding-left: 15px; margin-bottom: 20px; }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #e2e8f0;
            }}
            th {{ background-color: #f1f5f9; font-weight: 600; }}
            .grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
            }}
            .persona {{
                border: 1px solid #e2e8f0;
                padding: 20px;
                border-radius: 8px;
                background: #fdfdfd;
            }}
            .badge {{
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                background: var(--primary);
                color: white;
                font-size: 0.8rem;
                margin-bottom: 10px;
            }}
            .strategy {{
                background: #f0fdf4;
                border: 1px solid #bbf7d0;
                padding: 15px;
                border-radius: 6px;
                margin-top: 15px;
                font-weight: 500;
            }}
            img {{
                max-width: 100%;
                border-radius: 8px;
                margin-top: 20px;
            }}
            .footer {{
                text-align: center;
                margin-top: 60px;
                color: var(--secondary);
                font-size: 0.9rem;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>🛍️ Dự Án Phân Khúc Khách Hàng</h1>
                <p>Báo cáo kết quả kết hợp Association Rules & RFM Clustering</p>
            </header>

            <section class="card">
                <h2>1. Trực Quan Hóa Phân Cụm (PCA)</h2>
                <p>Bản đồ PCA 2D giúp quan sát mức độ tách biệt giữa các nhóm khách hàng dựa trên hành vi mua sắm và giá trị giao dịch.</p>
                <img src="data:image/png;base64,{pca_base64}" alt="PCA Plot">
            </section>

            <section class="card">
                <h2>2. Thống Kê Chỉ Số RFM Theo Cụm</h2>
                {df_rfm.to_html(index=False, classes='table')}
            </section>

            <section class="card">
                <h2>3. Chân Dung Khách Hàng & Chiến Lược</h2>
                <div class="grid">
    """

    for cid, p in personas.items():
        html_content += f"""
                    <div class="persona">
                        <span class="badge">Cụm {cid}</span>
                        <h3>{p['name']}</h3>
                        <p>{p['desc']}</p>
                        <div class="strategy">💡 Chiến lược: {p['strategy']}</div>
                    </div>
        """

    html_content += """
                </div>
            </section>

            <section class="card">
                <h2>4. Top Quy Luật Mua Sắm Theo Cụm</h2>
                <p>Các luật kết hợp (Association Rules) có chỉ số Lift cao nhất được kích hoạt trong từng cụm.</p>
    """

    for cid in df_rules['cluster'].unique():
        cluster_rules = df_rules[df_rules['cluster'] == cid].head(5)
        html_content += f"<h3>Gợi ý cho Cụm {cid}</h3>"
        html_content += cluster_rules[['rule', 'lift']].to_html(index=False, classes='table')

    html_content += f"""
            </section>

            <section class="card">
                <h2>5. Nâng Cấp: So Sánh Đa Mô Hình</h2>
                <p>So sánh hiệu quả giữa KMeans và Agglomerative Clustering qua các chỉ số Silhouette, DBI và CH Index.</p>
                {df_model.to_html(index=False, classes='table')}
            </section>

            <div class="footer">
                &copy; 2026 Mini Project - Data Mining | Được tạo tự động bởi Antigravity AI
            </div>
        </div>
    </body>
    </html>
    """

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated report: {REPORT_PATH}")

if __name__ == "__main__":
    generate_html()
