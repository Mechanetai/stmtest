import streamlit as st
import math
from decimal import Decimal, ROUND_HALF_UP


def input_float_(info: str, help=None):
    try:
        value = float(st.text_input(info, help=help))
        return value
    except Exception:
        pass


def input_int_(info: str):
    try:
        value = int(st.text_input(info))
        return value
    except Exception:
        pass


def decimal_half_up(num, fig='0.001'):
    decinum = Decimal(str(num)).quantize(Decimal(fig), rounding=ROUND_HALF_UP)
    return decinum


@st.cache
def efsz_r_ttest(t_value: float, dof: float):
    numerator_ = t_value**2
    denominator_ = t_value**2 + dof
    efsz_r = math.sqrt(numerator_ / denominator_)
    return efsz_r


@st.cache
def efsz_d_ttest(mean_a, mean_b, sd_a, sd_b, n_a, n_b):
    numerator_ = abs(mean_a-mean_b)
    denominator_ = math.sqrt(((n_a-1)*(sd_a**2)+(n_b-1)*(sd_b**2))/(n_a+n_b-2))
    efsz_d = numerator_/denominator_
    return efsz_d


@st.cache
def efsz_g_ttest():
    pass


@st.cache
def delta_ttest():
    pass


def es_r_t():
    t_value = st.number_input("t値", format="%.5f")
    dof = st.number_input("自由度", format="%.5f")

    try:
        es_r = efsz_r_ttest(t_value, dof)
        st.write("効果量r: ", es_r)
    except ZeroDivisionError:
        st.markdown("ZeroDivisionError: ")
    except Exception:
        st.markdown("不明なエラー: ")


def es_d_t():
    mean_a = input_float_("群1の平均値")
    mean_b = input_float_("群2の平均値")
    st_a = input_float_("群1の標準偏差")
    st_b = input_float_("群2の標準偏差")
    n_a = input_int_("群1のn数")
    n_b = input_int_("群1のn数")

    if not (mean_a == mean_b == st_a == st_b == 0 and n_a == n_b == 1):
        try:
            es_d = efsz_d_ttest(mean_a, mean_b, st_a, st_b, n_a, n_b)
            st.write("効果量d: ", decimal_half_up(es_d), " (", es_d, ")")
        except ZeroDivisionError:
            st.warning("ZeroDivisionError")
        except Exception as e:
            st.warning("不明なエラー")
            st.write(e)
    else:
        st.info("上の欄すべてに数値を入力して下さい")


def es_g_t():
    pass


if __name__ == '__main__':
    print("test")
