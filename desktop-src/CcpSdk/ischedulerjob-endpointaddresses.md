---
Description: 'Retrieves a collection of endpoint addresses that you can use to connect to a shared session.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0630930d-d888-4a50-90f3-11fec0863a9c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::EndpointAddresses property'
---

# ISchedulerJob::EndpointAddresses property

Retrieves a collection of endpoint addresses that you can use to connect to a shared session.

This property is read-only.

## Syntax


```C++
HRESULT get_EndpointAddresses(
  [out] IStringCollection **pAddresses
);
```



## Property value

An [**IStringCollection**](istringcollection.md) interface that contains a collection of endpoint addresses.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) job property.

## Remarks

This property is used by SOA-based client applications that want to connect to a shared session.

The collection can contain up to two addresses. The number of addresses depends on the transport schemes specified when the client created the session. The address that you use depends on the binding that you want to use to bind your client proxy to the broker. If you want to use NetTcp, use the address that contains net.tcp://. If you want to use Http, use the address that contains http://.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




