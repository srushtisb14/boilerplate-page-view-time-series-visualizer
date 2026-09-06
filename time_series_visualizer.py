

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def draw_line_plot():
    # Import data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

    # Clean data
    df = df[
        (df["value"] >= df["value"].quantile(0.025))
        & (df["value"] <= df["value"].quantile(0.975))
    ]

    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df["value"])

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")

    return fig


def draw_bar_plot():
    # Copy and prepare data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])

    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    df = df[
        (df["value"] >= df["value"].quantile(0.025))
        & (df["value"] <= df["value"].quantile(0.975))
    ]

    df_bar = df.groupby(["year", "month"])["value"].mean().unstack()

    fig = df_bar.plot.bar(figsize=(10, 7)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        title="Months",
    )

    fig.savefig("bar_plot.png")

    return fig


def draw_box_plot():
    # Prepare data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])

    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.strftime("%b")

    df = df[
        (df["value"] >= df["value"].quantile(0.025))
        & (df["value"] <= df["value"].quantile(0.975))
    ]

    # Create plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(data=df, x="year", y="value", ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    sns.boxplot(
        data=df,
        x="month",
        y="value",
        order=month_order,
        ax=axes[1],
    )

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")

    return fig
    