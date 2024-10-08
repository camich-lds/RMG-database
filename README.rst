*******************************************
RMG-database - A chemistry database for RMG
*******************************************
Edit:

This fork of the RMG-database is a modified version of an older database branch. It can be used to produce mechanisms for oxygenated species, which perform better than those produced using the main branch database. The database cannot currently be contributed to the main branch without additional work to extract the new training data and groups, as several reaction families are substantially different to those in the current main branch database.  

Database expanded for the generation of oxygenated species mechanisms. Expansion performed using pre-existing resources and literature data.
For more information see the following publications:

Christian Michelbach, Khaiyom Hakimov, Aamir Farooq, Alison S. Tomlin,
Predicting the autoignition behaviour of tailorable advanced biofuel blends using automatically generated mechanisms,
Proceedings of the Combustion Institute,
Volume 40, Issues 1–4,
2024,
105667,
ISSN 1540-7489,
https://doi.org/10.1016/j.proci.2024.105667

Christian Michelbach, Alison S. Tomlin,
Automatic mechanism generation for the combustion of advanced biofuels: A case study for diethyl ether,
International Journal of Chemical Kinetics,
Volume 56, Issue 4,
2024,
233-262,
ISSN 1097-4601,
https://doi.org/10.1002/kin.21705

If used, please cite the database using either or both of the above citations.

Original RMG-database README:

Authors: Prof. William H. Green (whgreen@mit.edu), Prof. Richard H. West (r.west@neu.edu) 
and the RMG Team (rmg_dev@mit.edu)

This repository contains the database of chemical information used by Reaction
Mechanism Generator (RMG) to determine the chemical parameters needed by its
generated chemistry models.

See the `RMG-Py repository for links to our documentation <https://github.com/ReactionMechanismGenerator/RMG-Py>`_.

