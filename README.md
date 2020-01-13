# COSE-Serverless-Configuration
### COSE: Configuring Serverless Functions using Statistical Learning

### Abstract:
Serverless  computing  has  emerged  as  a  new  compelling paradigm for the deployment of applications and services. It  represents  an  evolution  of  cloud  computing  with  a  simplified programming model, that aims to abstract away most operational concerns. Running serverless functions requires users to configure multiple parameters, such as memory, CPU, cloud provider, etc. While  relatively  simpler,  configuring  such  parameters  correctly while minimizing cost and meeting delay   constraints is not trivial. In   this   paper,   we   present   COSE, a framework that uses Bayesian Optimization to find the optimal configuration for serverless functions. COSE uses statistical learning techniques to intelligently  collect  samples and  predict  the  cost  and  execution time of a serverless function across unseen configuration values. Our  framework  uses  the  predicted  cost  and  execution  time,  to select  the  “best”  configuration  parameters  for  running  a  single or  a  chain  of  functions,  while  satisfying  customer  objectives. In  addition,  COSE  has  the  ability  to  adapt  to  changes  in  the execution  time  of  a  serverless  function. We  evaluate  COSE  not only on a commercial cloud provider, where we successfully found optimal/near-optimal  configurations  in  as  few  as  five  samples, but   also   over   a   wide   range   of   simulated   distributed   cloud environments  that  confirm  the  efficacy  of  our  approach.

### Publications:
- Nabeel Akhtar, Ali Raza, Vatche Ishakian and Ibrahim Matta<br>
**COSE: Configuring Serverless Functions using Statistical Learning**<br>
To appear at *IEEE International Conference on Computer Communications (INFOCOM), 2020, Beijing, China, April 2020*
