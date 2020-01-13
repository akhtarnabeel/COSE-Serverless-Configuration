# COSE-Serverless-Configuration
### COSE: Configuring Serverless Functions using Statistical Learning

### Abstract:
Serverless  computing  has  emerged  as  a  new  com-pelling paradigm for the deployment of applications and services.It  represents  an  evolution  of  cloud  computing  with  a  simplifiedprogramming model, that aims to abstract away most operationalconcerns. Running serverless functions requires users to configuremultiple parameters, such as memory, CPU, cloud provider,etc.While  relatively  simpler,  configuring  such  parameters  correctlywhile   minimizing   cost   and   meeting   delay   constraints   is   nottrivial.   In   this   paper,   we   present   COSE,   a   framework   thatuses Bayesian Optimization to find the optimal configuration forserverless functions. COSE uses statistical learning techniques tointelligently  collect  samples  and  predict  the  cost  and  executiontime of a serverless function across unseen configuration values.Our  framework  uses  the  predicted  cost  and  execution  time,  toselect  the  “best”  configuration  parameters  for  running  a  singleor  a  chain  of  functions,  while  satisfying  customer  objectives.In  addition,  COSE  has  the  ability  to  adapt  to  changes  in  theexecution  time  of  a  serverless  function.  We  evaluate  COSE  notonly on a commercial cloud provider, where we successfully foundoptimal/near-optimal  configurations  in  as  few  as  five  samples,but   also   over   a   wide   range   of   simulated   distributed   cloudenvironments  that  confirm  the  efficacy  of  our  approach.

### Publications:
- Nabeel Akhtar, Ali Raza, Vatche Ishakian and Ibrahim Matta<br>
**COSE: Configuring Serverless Functions using Statistical Learning**<br>
To appear at *IEEE International Conference on Computer Communications (INFOCOM), 2020, Beijing, China, April 2020*
