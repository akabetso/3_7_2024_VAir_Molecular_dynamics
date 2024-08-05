# Protein Modification Stability Study using Molecular Dynamics

## Project Overview

This project was developed by VAir under the sponsorship and guidance of Sup'Biotech and Descartes Developpement et Innovation.

This project focuses on studying the stability of protein modification, particularly by incorporating a click reaction at the C-terminus of a protein. This allows a linker to be attached, facilitating the attachment of a single domain antibody (nanobody) to a gold surface. Given the stability of single domain nanobodies, our objective was to understand how modifications affect the protein's conformational stability and binding sites.

## Documentaton

You can view the documentation in the [Documentation.ipynb](https://github.com/akabetso/3_7_2024_VAir_Molecular_dynamics/blob/master/Documentation.ipynb) file.

## Goals

- **Study Conformational Changes**: Evaluate how protein modifications induce conformational changes.
- **Binding Site Analysis**: Assess the impact of modifications on the protein's binding sites.
- **Simulation Comparisons**: Test and validate our simulations against existing literature to ensure reproducibility.
- **Optimization of Linkers**: Experiment with different linkers to determine the most optimal one for attaching nanobodies to the gold surface.
- **Cost-Effective Pipeline**: Provide additional data to support wet lab findings, offering an overview of steric effects and immobilization position orientation.

## Methodology

### Tools and Software

- **NAMD**: Used for molecular dynamics simulations.
- **Quantum Force Fields**: Employed to model the protein accurately and compare conformational changes.
- **ChemDraw3D and Spaetran 24'**: used to design the linker for the click chemistry

### Steps

1. **Modification and Modeling**: Modify the protein to include a click reaction at its C-terminus.
2. **Simulation**: Perform molecular dynamics simulations using NAMD.
3. **Analysis**: Compare the conformational changes and binding site alterations pre- and post-modification.
4. **Validation**: Cross-check our simulations with other studies in literature to ensure reproducibility.
5. **Optimization**: Test various linkers to identify the most effective one for attaching the single domain nanobody to the gold surface.
6. **Preparation for Wet Lab**: Utilize simulation data to guide and support wet lab experiments.

## Results

- **Conformational Changes**: The modification induced significant conformational changes.
- **Binding Sites**: The modifications affected the binding sites of the protein.

## Future Work

- **Simulation Validation**: Continue testing other simulations from literature to further validate our pipeline.
- **Linker Optimization**: Experiment with additional linkers to select the most optimal for attachment.
- **Wet Lab Testing**: Begin wet lab experiments based on our simulation findings to validate our computational results.

## Installation

NAMD Linux Version 3.0b7 (2024-05-10) was downloaded and used for this work.

## Reference

1. Simões, B., Guedens, W. J., Keene, C., Kubiak-Ossowska, K., Mulheran, P., Kotowska, A. M., Scurr, D. J.,
Alexander, M. R., Broisat, A., Johnson, S., Muyldermans, S., Devoogdt, N., Adriaensens, P., & Mendes, P. M. (2021).
Direct Immobilization of Engineered Nanobodies on Gold Sensors. ACS applied materials & interfaces, 13(15),
17353–17360. https://doi.org/10.1021/acsami.1c02280
2. Singh, A. N., & Sharma, N. (2019). Epigenetic Modulators as Potential Multi-targeted Drugs Against Hedgehog
Pathway for Treatment of Cancer. The Protein Journal. doi:10.1007/s10930-019-09832-9
3. Hicks C, Dhiman A, Barrymore C, Goswami T. Traumatic Brain Injury Biomarkers, Simulations and Kinetics.
Bioengineering (Basel). 2022 Oct 25;9(11):612. doi: 10.3390/bioengineering9110612. PMID: 36354523; PMCID:
PMC9687153.
4. Liu, L., Cai, L., Chu, Y., & Zhang, M. (2022). Thermostability mechanisms of β-agarase by analyzing its structure
through molecular dynamics simulation. AMB Express, 12(1), 50. https://doi.org/10.1186/s13568-022-01394-x
5. Singh, A. N., & Sharma, N. (2019). Epigenetic Modulators as Potential Multi-targeted Drugs Against Hedgehog
Pathway for Treatment of Cancer. The Protein Journal. doi:10.1007/s10930-019-09832-9
6. Aslan, T., Yenenler-Kutlu, A., Gerlevik, U., Aktuğlu Zeybek, A. Ç., Kıykım, E., Sezerman, O. U., & Birgul Iyison, N.
(2021). Identifying and elucidating the roles of Y198N and Y204F mutations in the PAH enzyme through molecular
dynamic simulations. Journal of Biomolecular Structure and Dynamics, 1–12. doi:10.1080/07391102.2021.1921619
