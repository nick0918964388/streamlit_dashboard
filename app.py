import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 设置页面配置
st.set_page_config(page_title="ESG 平台", layout="wide")

# 侧边栏
with st.sidebar:
    st.title("tsmc ESG platform")
    st.sidebar.markdown("---")
    
    # 环境
    with st.expander("环境", expanded=True):
        st.button("温室气体")
        st.button("能源管理")
        st.button("水资源管理")
        st.button("废弃物管理")
        st.button("空气污染防制")
    
    # 社会
    with st.expander("社会", expanded=True):
        st.button("人力资源")
        st.button("职业健康与安全")
        st.button("供应链管理")
        st.button("社区参与")
    
    # 治理
    with st.expander("治理", expanded=True):
        st.button("公司治理")
        st.button("风险管理")
        st.button("商业道德")
        st.button("信息安全")
    
    # 管理功能
    with st.expander("管理功能", expanded=True):
        st.button("数据分析")
        st.button("报告生成")
        st.button("设置")

# 主页面
st.title("Dashboard")

# 搜索栏
st.text_input("搜索 ESG 指标...")

# 标签页
tab1, tab2, tab3, tab4 = st.tabs(["概览", "循环", "社会", "治理"])

with tab1:
    # 创建三列布局
    col1, col2, col3 = st.columns(3)

    # 温室气体排放
    with col1:
        st.subheader("温室气体排放")
        st.write("追踪温室气体排放量及减量目标的达成率。")
        st.metric(label="2024年目标", value="减少10%", delta="减少8%")

    # 水资源管理
    with col2:
        st.subheader("水资源管理")
        st.write("优化制程用水重复使用率的用水和回收利用。")
        st.metric(label="2024年目标", value="回收率85%", delta="回收率82%")

    # 能源管理
    with col3:
        st.subheader("能源管理")
        st.write("提高能源效率和管理中的能源公用。")
        st.metric(label="2024年目标", value="效率提升15%", delta="效率提升12%")

    # 第二行
    col4, col5, col6 = st.columns(3)

    # 零废弃管理
    with col4:
        st.subheader("零废弃管理")
        st.write("量化零废弃物管理，最大化资源回收和利用。")
        st.metric(label="2024年目标", value="回收率95%", delta="回收率92%")

    # 空气污染防制
    with col5:
        st.subheader("空气污染防制")
        st.write("管控各类空气污染物的空气污染防制。")
        st.metric(label="2024年目标", value="减排20%", delta="减排18%")

    # 绩效索
    with col6:
        st.subheader("绩效索")
        st.write("所有评估绩效指标，用于建筑能源效率。")
        st.metric(label="2024年目标", value="90%绿建筑认证", delta="85%绿建筑认证")

    # ESG 绩效趋势图
    st.subheader("ESG 绩效趋势")
    
    # 创建示例数据
    months = ['1月', '2月', '3月', '4月', '5月', '6月']
    data1 = [85, 88, 90, 92, 93, 95]
    data2 = [80, 82, 85, 87, 88, 90]
    data3 = [75, 78, 80, 82, 83, 85]

    # 创建图表
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=data1, mode='lines+markers', name='指标1'))
    fig.add_trace(go.Scatter(x=months, y=data2, mode='lines+markers', name='指标2'))
    fig.add_trace(go.Scatter(x=months, y=data3, mode='lines+markers', name='指标3'))

    fig.update_layout(
        xaxis_title="月份",
        yaxis_title="绩效指标",
        legend_title="指标类型",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

# 运行 Streamlit 应用
if __name__ == "__main__":
    st.run()