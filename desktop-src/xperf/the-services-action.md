---
title: The Services Action
description: The Services Action
ms.assetid: 'fc1c8f9a-ad1a-4964-a5ce-816c5a0f9da5'
---

# The Services Action

The services action produces a text file that summarizes the various metrics regarding services. The usage for this action is:


```
-a Services [-range T1 T2] [-poiThreshold...] 
```





| Option                                    | Description                                                                             |
|-------------------------------------------|-----------------------------------------------------------------------------------------|
| range T1 T2 <br/>                   | Show data between times T1 and T2 (both in usec) <br/>                            |
| poiThreshold\_ContainerInit T <br/> | Flag any container init time greater than T (in usec) as a point of interest<br/> |
| poiThreshold\_ImageLoad T <br/>     | Flag any image load time greater than T (in usec) as a point of interest<br/>     |
| poiThreshold\_ServiceInit T <br/>   | Flag any service init time greater than T (in usec) as a point of interest<br/>   |



 

The default is to not flag any services as points of interest. All times are displayed in milliseconds.

 

 





