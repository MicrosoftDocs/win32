---
description: 'The Xenroll.dll library contains the following methods and properties that you can use to manage certificate stores.FunctionsDescriptionCAStoreFlagsSpecifies or returns flags that control access to the certification authority (CA) store.CAStoreNameWStrSpecifies or returns the name of the CA store.CAStoreTypeWStrSpecifies or returns the type of the store identified by the CAStoreName property.MyStoreFlagsSpecifies or returns a flag that determines the path of the personal store.MyStoreNameWStrSpecifies or returns the name of the personal store.MyStoreTypeWStrSpecifies or returns the type of the personal store.RequestStoreFlagsSpecifies or returns a flag that determines the path of the request store.RequestStoreNameWStrSpecifies or returns the name of the request store.RequestStoreTypeWStrSpecifies or returns the type of the request store.RootStoreFlagsSpecifies or returns a flag that determines the path of the root store.RootStoreNameWStrSpecifies or returns the name of the root store.RootStoreTypeWStrSpecifies or returns the type of the root store.SetHStoreCASpecifies the handle of the CA store.SetHStoreMySpecifies the handle of the personal store.SetHStoreRequestSpecifies the handle of the request store.SetHStoreROOTSpecifies the handle of the root store. '
ms.assetid: 15e4368b-4199-415a-9c2c-2c1351b717e6
title: Certificate Store Functions
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Store Functions

The Xenroll.dll library contains the following methods and properties that you can use to manage certificate stores.

| Functions                                                          | Description                                                                                                                                                                                          |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CAStoreFlags**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_castoreflags)                 | Specifies or returns flags that control access to the [*certification authority*](/windows/desktop/SecGloss/c-gly) (CA) store.<br/> |
| [**CAStoreNameWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_castorenamewstr)           | Specifies or returns the name of the CA store.<br/>                                                                                                                                            |
| [**CAStoreTypeWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_castoretypewstr)           | Specifies or returns the type of the store identified by the **CAStoreName** property.<br/>                                                                                                    |
| [**MyStoreFlags**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_mystoreflags)                 | Specifies or returns a flag that determines the path of the personal store.<br/>                                                                                                               |
| [**MyStoreNameWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_mystorenamewstr)           | Specifies or returns the name of the personal store.<br/>                                                                                                                                      |
| [**MyStoreTypeWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_mystoretypewstr)           | Specifies or returns the type of the personal store.<br/>                                                                                                                                      |
| [**RequestStoreFlags**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_requeststoreflags)       | Specifies or returns a flag that determines the path of the request store.<br/>                                                                                                                |
| [**RequestStoreNameWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_requeststorenamewstr) | Specifies or returns the name of the request store.<br/>                                                                                                                                       |
| [**RequestStoreTypeWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_requeststoretypewstr) | Specifies or returns the type of the request store.<br/>                                                                                                                                       |
| [**RootStoreFlags**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_rootstoreflags)             | Specifies or returns a flag that determines the path of the root store.<br/>                                                                                                                   |
| [**RootStoreNameWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_rootstorenamewstr)       | Specifies or returns the name of the root store.<br/>                                                                                                                                          |
| [**RootStoreTypeWStr**](/windows/desktop/api/xenroll/nf-xenroll-ienroll-get_rootstoretypewstr)       | Specifies or returns the type of the root store.<br/>                                                                                                                                          |
| [**SetHStoreCA**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-sethstoreca)                   | Specifies the handle of the CA store.<br/>                                                                                                                                                     |
| [**SetHStoreMy**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-sethstoremy)                   | Specifies the handle of the personal store.<br/>                                                                                                                                               |
| [**SetHStoreRequest**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-sethstorerequest)         | Specifies the handle of the request store.<br/>                                                                                                                                                |
| [**SetHStoreROOT**](/windows/desktop/api/xenroll/nf-xenroll-ienroll2-sethstoreroot)               | Specifies the handle of the root store.<br/>                                                                                                                                                   |



 

CertEnroll.dll does not export functionality that enables you to specify or retrieve store property values or copy certificates to specific stores.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> </dl>

 

