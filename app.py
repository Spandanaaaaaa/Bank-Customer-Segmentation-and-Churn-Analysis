
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Bank Customer Analytics",
    page_icon="🏦",
    layout="wide"
)

# ---------------- LOAD DATA ----------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/segmented_bank_customers.csv")

    df["CustomerSegment"] = pd.to_numeric(
        df["CustomerSegment"], errors="coerce"
    )

    df["Exited"] = pd.to_numeric(df["Exited"], errors="coerce")
    return df

df = load_data()

# ---------------- HEADER ----------------

st.title("🏦 Bank Customer Segmentation & Churn Analysis")
st.markdown(
    "Interactive banking analytics dashboard | "
    "Customer insights | Retention | Segmentation"
)

st.divider()

# ---------------- SIDEBAR FILTERS ----------------

st.sidebar.title("🔎 Dashboard Filters")

st.sidebar.caption("Filter customer data below.")

geography = st.sidebar.selectbox(
    "Geography",
    ["All"] + sorted(df["Geography"].dropna().unique().tolist())
)

gender = st.sidebar.selectbox(
    "Gender",
    ["All"] + sorted(df["Gender"].dropna().unique().tolist())
)

age_range = st.sidebar.slider(
    "Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (int(df["Age"].min()), int(df["Age"].max()))
)

segments = sorted(
    df["CustomerSegment"].dropna().unique().tolist()
)

segment = st.sidebar.selectbox(
    "Customer Segment",
    ["All"] + segments
)

activity = st.sidebar.selectbox(
    "Activity Status",
    ["All", "Active", "Inactive"]
)

credit_card = st.sidebar.selectbox(
    "Credit Card",
    ["All", "Yes", "No"]
)

# ---------------- APPLY FILTERS ----------------

filtered_df = df.copy()

if geography != "All":
    filtered_df = filtered_df[
        filtered_df["Geography"] == geography
    ]

if gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == gender
    ]

filtered_df = filtered_df[
    filtered_df["Age"].between(age_range[0], age_range[1])
]

if segment != "All":
    filtered_df = filtered_df[
        filtered_df["CustomerSegment"] == segment
    ]

if activity != "All":
    activity_value = 1 if activity == "Active" else 0
    filtered_df = filtered_df[
        filtered_df["IsActiveMember"] == activity_value
    ]

if credit_card != "All":
    card_value = 1 if credit_card == "Yes" else 0
    filtered_df = filtered_df[
        filtered_df["HasCrCard"] == card_value
    ]

# ---------------- KPI METRICS ----------------

st.subheader("📊 Key Performance Indicators")

total_customers = len(filtered_df)

churned_customers = int(
    (filtered_df["Exited"] == 1).sum()
)

churn_rate = (
    churned_customers / total_customers * 100
    if total_customers > 0 else 0
)

retention_rate = 100 - churn_rate

average_balance = (
    filtered_df["Balance"].mean()
    if total_customers > 0 else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churned Customers", f"{churned_customers:,}")
col3.metric("Churn Rate", f"{churn_rate:.2f}%")
col4.metric("Retention Rate", f"{retention_rate:.2f}%")

col5, col6 = st.columns(2)

col5.metric("Average Balance", f"₹{average_balance:,.2f}")
col6.metric(
    "Active Customers",
    f"{int((filtered_df['IsActiveMember'] == 1).sum()):,}"
)

st.divider()

# ---------------- CHARTS ----------------

if filtered_df.empty:

    st.warning("No customers found for the selected filters.")

else:

    # Churn by Geography
    st.subheader("🌍 Churn Analysis by Geography")

    geo_data = (
        filtered_df.groupby(
            ["Geography", "Exited"]
        ).size().reset_index(name="Customers")
    )

    geo_data["Customer Status"] = geo_data["Exited"].map({
        0: "Retained",
        1: "Churned"
    })

    fig1 = px.bar(
        geo_data,
        x="Geography",
        y="Customers",
        color="Customer Status",
        barmode="group",
        title="Retained vs Churned Customers by Geography"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # Churn by Age Group
    st.subheader("👥 Churn Analysis by Age Group")

    age_data = filtered_df.copy()

    age_data["Age Group"] = pd.cut(
        age_data["Age"],
        bins=[17, 29, 39, 49, 59, 100],
        labels=["18-29", "30-39", "40-49", "50-59", "60+"]
    )

    age_summary = (
        age_data.groupby(
            ["Age Group", "Exited"], observed=False
        ).size().reset_index(name="Customers")
    )

    age_summary["Customer Status"] = age_summary["Exited"].map({
        0: "Retained",
        1: "Churned"
    })

    fig2 = px.bar(
        age_summary,
        x="Age Group",
        y="Customers",
        color="Customer Status",
        barmode="group",
        title="Customer Churn Across Age Groups"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # Customer Segments
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 Customer Segmentation")

        segment_data = (
            filtered_df["CustomerSegment"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        segment_data.columns = ["Segment", "Customers"]

        fig3 = px.pie(
            segment_data,
            names="Segment",
            values="Customers",
            hole=0.45,
            title="Customer Distribution by Segment"
        )

        st.plotly_chart(fig3, use_container_width=True)

    # Churn by Activity
    with col2:
        st.subheader("⚡ Customer Activity Analysis")

        activity_data = (
            filtered_df.groupby(
                ["IsActiveMember", "Exited"]
            ).size().reset_index(name="Customers")
        )

        activity_data["Activity"] = activity_data[
            "IsActiveMember"
        ].map({
            0: "Inactive",
            1: "Active"
        })

        activity_data["Customer Status"] = activity_data[
            "Exited"
        ].map({
            0: "Retained",
            1: "Churned"
        })

        fig4 = px.bar(
            activity_data,
            x="Activity",
            y="Customers",
            color="Customer Status",
            barmode="group",
            title="Churn by Activity Status"
        )

        st.plotly_chart(fig4, use_container_width=True)

    # Balance Analysis
    st.subheader("💰 Customer Balance Analysis")

    fig5 = px.box(
        filtered_df,
        x="CustomerSegment",
        y="Balance",
        color="CustomerSegment",
        title="Balance Distribution Across Customer Segments"
    )

    st.plotly_chart(fig5, use_container_width=True)

    # Customer Table
    st.subheader("📋 Customer Details")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    # Download Filtered Data
    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Filtered Customer Data",
        data=csv,
        file_name="filtered_bank_customers.csv",
        mime="text/csv"
    )

# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "Bank Customer Analytics Project | "
    "Built using Python, Pandas, Plotly and Streamlit. "
    "Dataset is synthetic and created for educational purposes."
)
