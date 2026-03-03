# Bayesian assessment of chlorofluorocarbon (CFC), hydrochlorofluorocarbon (HCFC) and halon banks

## Terms and Definitions
### Banks
The reservoirs of chemicals that are present in old equipments that continue to emit the chemical compounds. For e.g: refrigerators, air conditioners, foams, and fire extinguishers.

1. Short-term Banks: Fully emitted within the first 2 years after production
2. Medium-term Banks: Lose about 10%-20% of their material each year
3. Long-term Banks: Can lose as little as 2 % of their material each year

## Modeling approaches
### Top down
Banks are estimated as the cumulative difference between reported production and observationally derived emissions. 
Banks = Reported Production - Observed Emissions
#### Caveats
* Reported production is often lower than actual. This can cause biases in bank estimations.
* Observed Emissions Estimates assumes that we know the global lifetimes which also has large uncertainty.

### Bottom Up
The equipment sales are compiled and the emission rates from each equipment is estimated. This information in used to estimate emissions and banks.
#### Caveats
* The sales data is not accurate.
* The emission rates are an approximation and can vary depending on various factors.
* The observed atmospheric concentrations are not used in the analysis

### Hybrid
The hybrid approach uses a comprehensive *bottom up* survey from year 2008 as starting point. The future banks are calculated as a function of reported production (addition) and observationally derived emissions (subtraction).
#### Caveats
The farther you move from the survey year of 2008, the associated uncertainties in estimations also grows.

### Bayesian 
A *bottom-up* deterministic simulation model (DSM) is used to estimate the emissions. The DSM uses input parameters from previously published values, accounting for large uncertainties in production and bank release rates. It simultaneously models banks, emissions, and atmospheric concentrations. Parameters in the DSM are then conditioned (or updated) on observed concentrations by applying Bayes’ rule. The final result is a posterior distribution of banks by chemical and equipment type, along with an updated estimate of production and release rates for each equipment type. This approach incorporates data and assumptions from both the bottom-up and top-down approaches, providing a simulation model consistent with the bottom-up accounting method while also being consistent with observed concentrations within their uncertainties.
#### Caveats
* Higher computational costs

## Data
### Alternative Fluorocarbons Environmental Acceptability Study (AFEAS)
* Report global annual production up to 2001, categorized by equipment type, which is generally grouped as short, medium and long banks. 
### United Nations Environmental Programme’s (UNEP) global production
### Halocarbons used for feedstock production are available annually (UNEP/TEAP, 2021)

We use AFEAS data and categorization to develop our production priors and adopt the WMO (2003) correction where AFEAS production values are used up until 1989 and then scaled to match the United Nations Environmental Programme’s (UNEP) global production values for all years following 1989. 

## Website introduction
Halocarbons are synthetic compounds composed of carbon bonded to halogen atoms such as chlorine, fluorine, and bromine. Their chemical stability, low toxicity, and non-flammability led to widespread use during the 20th century in refrigeration and air conditioning, aerosol propellants, foam production, and fire suppression. For decades, these compounds were considered environmentally benign. This view changed in the 1970s, when atmospheric research showed that many halocarbons are long-lived and can reach the stratosphere, where ultraviolet radiation breaks them apart and releases chlorine and bromine. These atoms catalytically destroy ozone, allowing increased levels of harmful ultraviolet radiation to reach Earth’s surface.

The global consequences of halocarbon emissions became clear in the mid-1980s with the discovery of severe ozone depletion over Antarctica. In response, the international community adopted the Montreal Protocol on Substances that Deplete the Ozone Layer in 1987. The agreement established binding controls on the production and use of ozone-depleting substances, with phased timelines and support for developing countries. The Montreal Protocol has driven large reductions in atmospheric halocarbons and remains one of the most successful environmental treaties to date, though continued monitoring is essential as legacy emissions and emerging compounds persist.

Estimating halocarbon emissions and remaining banks has traditionally relied on either bottom-up accounting methods based on reported production, equipment inventories, and assumed leakage rates, or top-down approaches that infer emissions from atmospheric observations and lifetimes. Both methods are subject to substantial uncertainties arising from reporting biases, poorly constrained release rates, and uncertainties in atmospheric lifetimes. The Bayesian framework applied here integrates reported production, prior knowledge of emission processes, and atmospheric concentration measurements within a single probabilistic model. By conditioning simulated banks and emissions on observed atmospheric data, this approach provides statistically consistent estimates of production, emissions, and remaining banks, along with quantified uncertainties.

Here is the relevant excerpts from the manuscript:
Previously published assessments typically rely on one of
three modeling approaches to estimate bank sizes and then
estimate emissions associated with these banks. In the “top-
down” approach (e.g., Montzka et al., 2003), banks are es-
timated as the cumulative difference between reported pro-
duction and observationally derived emissions. However, by
taking the cumulative sum of a small difference between two
large values, small biases in emissions or reported produc-
tion estimates can propagate into large biases in bank esti-
mates (Velders and Daniel, 2014). Some type of bias is thus
expected since total production has very likely been greater
than reported production due to both the under-reporting of
production (e.g., Gamlen et al., 1986; Montzka et al., 2018)
and the exclusion of point-of-production losses in reported
production values. Further estimates of emissions rely on ob-
served concentrations along with global lifetime estimates,
which have large uncertainties associated with them (Ko et
al., 2013).
The second approach relies on a “bottom-up” accounting
method (Ashford et al., 2004; Campbell et al., 2005) where
the inventory of sales by equipment type are carefully tallied
along with estimated release rates by application use. The
bottom-up approach also relies on sales data from surveys of
various equipment types and products as well as estimates of
their respective leakage rates (Campbell et al., 2005). These
are all subject to uncertainties, which contribute to uncertain-
ties in bottom-up bank estimates as well. A limitation of the
bottom-up accounting method is that observed atmospheric
concentrations are used only as a qualitative check and are
not explicitly accounted for in the analysis. Another impor-
tant limitation is that data used in this method are unobserved
and rather rely on estimated processes along with reported
data, such as production or sales of equipment. Thus any
bias in reporting could propagate into large biases in bank
estimates.
The third approach, and the one used in more recent ozone
assessments such as the World Meteorological Organization
(WMO, 2011, 2018, 2014), uses a hybrid approach to calcu-
late banks. Bottom-up banks estimated for 2008 are used as
a starting point for the calculations. These banks are taken
from Campbell et al. (2005) and represent interpolated val-
ues from the 2002 and 2015 estimates. The banks are then
brought forward to the present time by adding the cumulate
reported production and subtracting the cumulative obser-
vationally derived emission from 2008 through the present. 
This approach is consistent with 2008 bottom-up bank es-
timates by design, however, as time between 2008 and the
present has grown, the cumulative errors associated with the
top-down approach become larger.
The modeling approach applied in the present study relies
on Bayesian inference of banks (Lickley et al., 2020, 2021)
where banks are estimated using an approach called Bayesian
Parameter Estimation (BPE). In this approach, a simulation
model of the bottom-up method is developed, where prior
distributions of input parameters are constructed from pre-
viously published values, accounting for large uncertainties
in production and bank release rates. The simulation model
simultaneously models banks, emissions, and atmospheric
concentrations. Parameters in the simulation model are then
conditioned (or updated) on observed concentrations by ap-
plying Bayes’ rule. The final result is a posterior distribution
of banks by chemical and equipment type, along with an up-
dated estimate of production and release rates for each equip-
ment type. This approach incorporates data and assumptions
from both the bottom-up and top-down approaches, provid-
ing a simulation model consistent with the bottom-up ac-
counting method while also being consistent with observed
concentrations within their uncertainties.
The Bayesian modeling approach from Lickley et al. (2020,
2021) draws on a Bayesian analysis approach called
Bayesian melding, designed by Poole and Raftery (2000),
that allows us to apply inference to a deterministic simulation
model. We employ a version of this method that we hence-
forth refer to as the Bayesian Parameter Estimation (BPE),
which allows for input parameter uncertainty (Hong et al.,
2005; Bates et al., 2003). The model flow is implemented as
follows: first we develop a deterministic simulation model,
representing the “bottom-up” accounting method that simul-
taneously simulates banks, emissions, and mole fractions
for each chemical and equipment type. In this analysis, the
chemicals considered include CFC-11, CFC-12, CFC-113,
CFC-114, CFC-115, HCFC-22, HCFC-141b, HCFC-142b,
halon 1201, and halon 1311. Prior distributions for each of
the input parameters are based on previously published esti-
mates. We then specify the likelihood function as a function
of the difference between observed and simulated mole frac-
tions. Finally, we estimate posterior distributions of both the
input and output parameters by implementing Bayes’ Rule
using a sampling procedure. Each of the steps of the BPE are
described in more detail below.