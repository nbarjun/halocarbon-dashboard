import plotly.express as px
import numpy as np

def gas_to_label(g):
    g = g.lower()
    if g.startswith("h-"):
        label = f"Halon-{g[2:]}"
    else:
        label = g.upper()
    if label.endswith("B"):
        label = label[:-1] + "b"
    return label

def prod_to_label(g):
    g = g.lower()
    if g.startswith("h-"):
        label = f"Halon-{g[2:]}"
    else:
        label = g.upper()
    if label.endswith("B"):
        label = label[:-1] + "b"
    return label

about_gas = {}
about_gas['CFC-11'] = '''CFC-11 (trichlorofluoromethane, CCl₃F) is a fully halogenated chlorofluorocarbon that was historically used as a refrigerant, aerosol propellant, and foam-blowing agent. It is colorless, non-flammable, and highly stable in the troposphere, which allows it to persist long enough to reach the stratosphere. There, ultraviolet radiation photolyzes CFC-11, releasing chlorine atoms that participate in catalytic reactions that destroy stratospheric ozone. CFC-11 has an ozone depletion potential (ODP) of 1.0 (by definition, relative to itself) and a long atmospheric lifetime of roughly 45-55 years, making it particularly damaging to the ozone layer. Due to these impacts, its production and use were phased out globally under the Montreal Protocol, although monitoring continues because of its long lifetime and past evidence of unexpected emissions.
'''
about_gas['CFC-12'] = '''CFC-12 (dichlorodifluoromethane, CCl₂F₂) is a fully halogenated chlorofluorocarbon that was widely used as a refrigerant, aerosol propellant, and foam-blowing agent. It is colorless, non-flammable, and chemically very stable in the troposphere, allowing it to persist and be transported into the stratosphere. There, ultraviolet radiation photolyzes CFC-12, releasing chlorine atoms that catalytically destroy stratospheric ozone. CFC-12 has an ozone depletion potential (ODP) of about 0.82 (relative to CFC-11 = 1) and a long atmospheric lifetime of roughly 100 years, making it one of the most influential ozone-depleting substances historically. As a result, its production and use were phased out under the Montreal Protocol, though it remains present in the atmosphere due to its long lifetime.
'''
about_gas['CFC-113'] = '''CFC-113 (1,1,2-trichloro-1,2,2-trifluoroethane, C₂Cl₃F₃) is a fully halogenated chlorofluorocarbon that was primarily used as a solvent for precision cleaning, especially in the electronics and aerospace industries, as well as in some refrigeration applications. It is colorless, non-flammable, and chemically very stable in the troposphere, enabling long-range transport into the stratosphere. There, ultraviolet radiation photolyzes CFC-113, releasing chlorine atoms that participate in catalytic ozone-destruction cycles. CFC-113 has an ozone depletion potential (ODP) of approximately 0.8 (relative to CFC-11 = 1) and an atmospheric lifetime of roughly 80-90 years, making it a significant contributor to historical ozone loss. Due to these impacts, its production and use were phased out under the Montreal Protocol, though it remains detectable in the atmosphere because of its long lifetime.
'''
about_gas['CFC-114'] = '''CFC-114 (1,2-dichloro-1,1,2,2-tetrafluoroethane, C₂Cl₂F₄) is a fully halogenated chlorofluorocarbon that was used mainly as a refrigerant, as well as in aerosol propellants and foam-blowing applications. It is colorless, non-flammable, and extremely stable in the troposphere, allowing it to persist for long periods and be transported into the stratosphere. There, ultraviolet radiation photolyzes CFC-114, releasing chlorine atoms that catalytically destroy stratospheric ozone. CFC-114 has an ozone depletion potential (ODP) of approximately 0.7-0.8 (relative to CFC-11 = 1) and a very long atmospheric lifetime of about 180-190 years, making it one of the longer-lived ozone-depleting substances. Because of its strong and persistent impact on the ozone layer, CFC-114 was phased out under the Montreal Protocol, though it remains present in the atmosphere due to its long lifetime.
'''
about_gas['CFC-115'] = '''CFC-115 (chloropentafluoroethane, C₂ClF₅) is a fully halogenated chlorofluorocarbon that was used primarily as a refrigerant (R-115), often in blended refrigerants for low-temperature applications. It is colorless, non-flammable, and extremely chemically stable in the troposphere, which allows it to persist for centuries and be transported efficiently into the stratosphere. There, ultraviolet radiation photolyzes CFC-115, releasing chlorine atoms that participate in catalytic cycles that destroy stratospheric ozone. CFC-115 has an ozone depletion potential (ODP) of roughly 0.6 (relative to CFC-11 = 1) and an exceptionally long atmospheric lifetime of about 500-550 years, making it one of the longest-lived ozone-depleting substances regulated under the Montreal Protocol. Although its production has been phased out, its long lifetime means it will continue to contribute to stratospheric chlorine loading for centuries.
'''
about_gas['HCFC-22'] = '''HCFC-22 (chlorodifluoromethane, CHClF₂) is a hydrochlorofluorocarbon that was widely used as a refrigerant (R-22) and as a feedstock for fluoropolymer production. Unlike CFCs, HCFC-22 contains hydrogen, which makes it partially reactive in the troposphere and therefore shorter-lived than CFCs. Nevertheless, a fraction of emitted HCFC-22 reaches the stratosphere, where UV photolysis releases chlorine atoms that contribute to catalytic ozone destruction. HCFC-22 has a relatively low ozone depletion potential (ODP ≈ 0.05) compared to CFCs and an atmospheric lifetime of about 12 years, but it is still an ozone-depleting substance. As a result, HCFC-22 has been controlled and phased out under the Montreal Protocol, serving historically as a transitional replacement for CFCs. In addition, HCFC-22 is a potent greenhouse gas, contributing to climate warming despite its lower ODP.
'''
about_gas['HCFC-141b'] = '''HCFC-141b (1,1-dichloro-1-fluoroethane, C₂H₃Cl₂F) is a hydrochlorofluorocarbon that was used mainly as a foam-blowing agent and as a solvent, particularly as a replacement for CFC-11 in rigid polyurethane foams. Because it contains hydrogen, HCFC-141b is partially degraded in the troposphere, giving it a much shorter lifetime than CFCs, though a fraction still reaches the stratosphere. There, photolysis releases chlorine atoms that participate in catalytic ozone-destruction cycles. HCFC-141b has an ozone depletion potential (ODP) of about 0.11 (relative to CFC-11 = 1) and an atmospheric lifetime of roughly 9-10 years. Due to its ozone-depleting effects, HCFC-141b has been controlled and phased out under the Montreal Protocol, having served as a transitional substitute for higher-ODP CFCs.
'''
about_gas['HCFC-142b'] = '''HCFC-142b (1-chloro-1,1-difluoroethane, C₂H₃ClF₂) is a hydrochlorofluorocarbon that was used primarily as a foam-blowing agent and as a refrigerant, as well as a feedstock in fluoropolymer production. Because it contains hydrogen, HCFC-142b undergoes partial degradation in the troposphere, giving it a significantly shorter lifetime than CFCs, although a fraction still reaches the stratosphere. There, ultraviolet photolysis releases chlorine atoms that contribute to catalytic destruction of stratospheric ozone. HCFC-142b has an ozone depletion potential (ODP) of about 0.065 (relative to CFC-11 = 1) and an atmospheric lifetime of roughly 17-18 years. As an ozone-depleting substance, HCFC-142b has been controlled and phased out under the Montreal Protocol, having served as a transitional replacement for higher-ODP CFCs.
'''
about_gas['Halon-1211'] = '''Halon-1211 (bromochlorodifluoromethane, CBrClF₂) is a halogenated hydrocarbon that was widely used as a fire-extinguishing agent, particularly in portable fire extinguishers for aviation, military, and industrial applications. It is colorless, non-flammable, and chemically stable in the troposphere, allowing it to persist long enough to reach the stratosphere. There, ultraviolet radiation photolyzes Halon-1211, releasing bromine atoms, which are extremely efficient catalysts for stratospheric ozone destruction—significantly more effective on a per-atom basis than chlorine. Halon-1211 has an ozone depletion potential (ODP) of about 3.0 (relative to CFC-11 = 1) and an atmospheric lifetime of roughly 16 years. Due to its strong ozone-depleting impact, Halon-1211 was phased out under the Montreal Protocol, although recycled (“banked”) halon remains in limited use for critical fire-protection applications.
'''
about_gas['Halon-1301'] = '''Halon-1301 (bromotrifluoromethane, CBrF₃) is a halogenated hydrocarbon that was widely used as a fire-extinguishing agent, particularly in fixed fire-suppression systems for aviation, military, and critical industrial facilities. It is colorless, non-flammable, and chemically very stable in the troposphere, allowing it to persist long enough to reach the stratosphere. There, ultraviolet photolysis releases bromine atoms, which are extremely efficient in catalyzing ozone destruction, much more potent on a per-atom basis than chlorine from CFCs. Halon-1301 has an ozone depletion potential (ODP) of about 10 (relative to CFC-11 = 1) and an atmospheric lifetime of roughly 70 years. Due to its severe ozone-depleting effects, Halon-1301 was phased out under the Montreal Protocol, although existing stocks are still used in limited, critical applications where alternatives are not suitable.
'''
def build_trace_library_gas(gas_list):
    colors = px.colors.qualitative.Bold
    lib = {}
    for i, gas in enumerate(gas_list):
        lib[gas] = {
            "label": gas_to_label(gas),
            "line_color": colors[i % len(colors)],
            "line_style":"solid",
            "about": about_gas[gas_to_label(gas)],
            "uncertainty": 0
        }
    return lib


def build_trace_library_production():
    rep_prod_list = ['shortProd','mediumProd','longProd','feedStock','prod']
    est_prod_list = ['short','medium','long']
    uncert_list = np.concat([np.zeros(len(rep_prod_list),dtype='int'),\
                    np.ones(len(est_prod_list),dtype='int')])
    prod_label = ['Reported Short Bank','Reported Medium Bank','Reported Long Bank',\
                'Reported Feedstock','Reported Production',\
                'Estimated Short Bank','Estimated Medium Bank', 'Estimated Long Bank']
    prod_list = rep_prod_list + est_prod_list
    line_colors = px.colors.qualitative.Dark2[:len(rep_prod_list)]
    line_colors += line_colors
    line_styles = ['dot' if unc else 'solid' for unc in uncert_list]
    
    lib = {}
    for i in range(len(prod_list)):
        lib[prod_list[i]] = {
            "label": prod_label[i],
            "line_color": line_colors[i],\
            "line_style": line_styles[i],\
            "uncertainty": uncert_list[i]
        }
    return lib
