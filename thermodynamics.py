import utility
import math

# The actual usable screen size is (in pixel):
# WIDTH = 320
# HEIGHT = 222
# The number of line and columns visible at the same time in the interpreter is (based on 'M'):
# MAX_LINE = 16  # Python font size = small
# MAX_COLUMN = 42  # Python font size = small
# MAX_LINE = 12  # Python font size = large
# MAX_COLUMN = 29  # Python font size = large


def quality(y, yf, yg):
    x = (y - yf) / (yg - yf)

    print("x = {:,.6g}".format(x))
    print("x = {:,.6g}".format(x))

    if x > 1:
        utility.show("The substance is in superheated vapor state.")
    elif x == 1:
        utility.show("The substance is in saturated vapor state.")
    elif x < 1 and x > 0:
        utility.show("The substance is in mixture state.")
    elif x == 0:
        utility.show("The substance is in saturated liquid state.")
    elif x < 0:
        utility.show("The substance is in compressed liquid state.")


def linearInterpolation(x, x1, y1, x2, y2):
    y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    print("y = {:,.6g}".format(y))


def efficiency(QL, QH):
    eff = 1 - QL / QH
    print("\u03B7 = {:,.6g}".format(eff))


def efficiencyCar(TL, TH):
    eff = 1 - TL / TH
    print("\u03B7 carnot = {:,.6g}".format(eff))


def refCOP(QL, QH):
    cop = 1 / (QH / QL - 1)
    print("\u03B2 = {:,.6g}".format(cop))


def refCOPCar(TL, TH):
    cop = 1 / (TH / TL - 1)
    print("\u03B2 carnot = {:,.6g}".format(cop))


def pumpCOP(QL, QH):
    cop = 1 / (1 - QL / QH)
    print("\u03B2 = {:,.6g}".format(cop))


def pumpCOPCar(TL, TH):
    cop = 1 / (1 - TL / TH)
    print("\u03B2 carnot = {:,.6g}".format(cop))


def dsLiqSol(C, T1, T2):
    ds = C * math.ln(T2 / T1)
    print("\u0394s = {:,.6g} J.Kg-1.K-1".format(ds))


def dsGasCv(Cv, T1, T2, R, v1, v2):
    ds = Cv * math.ln(T2 / T1) + R * math.ln(v2 / v1)
    print("\u0394s = {:,.6g} J.Kg-1.K-1".format(ds))


def dsGasCp(Cp, T1, T2, R, P1, P2):
    ds = Cp * math.ln(T2 / T1) - R * math.ln(P2 / P1)
    print("\u0394s = {:,.6g} J.Kg-1.K-1".format(ds))


def adiaTurbineEff(h1, h2, h2r):
    eff = (h2r - h1) / (h2 - h1)
    print("s2 - s1 = {:,.6g}".format(eff))


def adiaPumpEff(h1, h2, h2r):
    eff = (h2 - h1) / (h2r - h1)
    print("s2 - s1 = {:,.6g}".format(eff))


def adiaNozzleEff(v, vr):
    eff = (vr ** 2) / (v ** 2)
    print("s2 - s1 = {:,.6g}".format(eff))


def enthalpyVariation(h1, h2):
    work = h1 - h2
    print("w(1->2) = {:,.6g} J.Kg-1".format(work))


def pressureVariation(v, P1, P2):
    work = v * (P1 - P2)
    print("w(1->2) = {:,.6g} J.Kg-1".format(work))


menu = [
    "quality: quality(y, yf, yg)",
    "linear interpolation: linearInterpolation(x, x1, y1, x2, y2)",
    "heat engine efficiency: efficiency(QL, QH)",
    "heat engine Carnot efficiency: efficiencyCar(TL, TH)",
    "refrigerator COP: refCOP(QL, QH)",
    "refrigerator Carnot COP: refCOPCar(TL, TH)",
    "heat pump COP: pumpCOP(QL, QH)",
    "heat pump Carnot COP: pumpCOPCar(TL, TH)",
    "\u0394s liquid/solid (Gibbs): dsLiqSol(C, T1, T2)",
    "\u0394s ideal gas with Cv (Gibbs): dsGasCv(Cv, T1, T2, R, v1, v2)",
    "\u0394s ideal gas with Cp (Gibbs): dsGasCp(Cp, T1, T2, R, P1, P2)",
    "work isentropic steady flow (enthalpy): enthalpyVariation(h1, h2)",
    "pump work isentropic steady flow: pressureVariation(v, P1, P2)",
    "adiabatic/isentropic turnine efficiency: adiaTurbineEff(h1, h2, h2r)",
    "adiabatic/isentropic pump-compressor efficiency: adiaPumpEff(h1, h2, h2r)",
    "adiabatic/isentropic nozzle efficiency: adiaNozzleEff(v, vr)",
]
utility.printMenu("Thermodynamics", menu)
