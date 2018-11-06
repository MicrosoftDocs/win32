---
title: ServiceMonikerSample
description: This sample shows a client which can be used with the TCP MetadataExchange sample. It utilizes WCF service moniker.
ms.assetid: cfcff5ee-c0e1-4694-831e-fed0bd0e9855
keywords:
- ServiceMonikerSample Windows Web Services API
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ServiceMonikerSample

This sample shows a client which can be used with the TCP MetadataExchange sample. It utilizes WCF service moniker.

-   [PurchaseOrderClient.vbs](#purchaseorderclientvbs)

## PurchaseOrderClient.vbs


```VB
set obj = GetObject("service:mexAddress='net.tcp://localhost/example/mex', address='net.tcp://localhost/example', contract='IPurchaseOrder', contractNamespace='http://example.org', binding=PurchaseOrderBinding, bindingNamespace='http://example.org'")
for i = 1 to 100
 orderId = obj.Order(i,"Pencil", date)
 Wscript.Echo orderId, date
Next 


```



 

 




