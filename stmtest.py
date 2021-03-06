import streamlit as st
import escal

st.set_page_config(page_title="EffectSizeJP", page_icon=None)

contents_ = {"効果量計算機": 1, "効果量について": 2}
analyzes = {"t検定": 1, "一元配置分散分析": 2}
efsz_ttest = {"Cohen's d": 1, "r": 2, "delta": 3}
efsz_anova = {"η^2": 1, "partial η^2": 2}

dd_info = '分析手法の選択'


def sidebar_(dd_info, dd_contents):
    selected_title = st.sidebar.selectbox(dd_info, list(dd_contents.keys()))
    return selected_title


def main():
    title_ = sidebar_('コンテンツを選択', contents_)
    st.title(title_)
    if contents_[title_] == 1:
        selected_analyzes = sidebar_(dd_info, analyzes)
        if analyzes[selected_analyzes] == 1:
            selected_efsz = sidebar_(dd_info, efsz_ttest)
            if efsz_ttest[selected_efsz] == 1:
                escal.es_d_t()
            elif efsz_ttest[selected_efsz] == 2:
                escal.es_r_t()
            elif efsz_ttest[selected_efsz] == 3:
                pass
        elif analyzes[selected_analyzes] == 2:
            selected_efsz = sidebar_(dd_info, efsz_anova)
            if efsz_anova[selected_efsz] == 1:
                pass
            elif efsz_anova[selected_efsz] == 2:
                pass
    elif contents_[title_] == 2:
        st.success('This is a success message!')
        with open("EffectSize.md", encoding="utf-8") as f:
            md = f.read()
        st.title('効果量について')
        st.markdown(md)


main()
