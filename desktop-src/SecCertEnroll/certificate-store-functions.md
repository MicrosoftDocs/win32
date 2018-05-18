---
Description: 'The Xenroll.dll library contains the following methods and properties that you can use to manage certificate stores.FunctionsDescriptionCAStoreFlagsSpecifies or returns flags that control access to the certification authority (CA) store.CAStoreNameWStrSpecifies or returns the name of the CA store.CAStoreTypeWStrSpecifies or returns the type of the store identified by the CAStoreName property.MyStoreFlagsSpecifies or returns a flag that determines the path of the personal store.MyStoreNameWStrSpecifies or returns the name of the personal store.MyStoreTypeWStrSpecifies or returns the type of the personal store.RequestStoreFlagsSpecifies or returns a flag that determines the path of the request store.RequestStoreNameWStrSpecifies or returns the name of the request store.RequestStoreTypeWStrSpecifies or returns the type of the request store.RootStoreFlagsSpecifies or returns a flag that determines the path of the root store.RootStoreNameWStrSpecifies or returns the name of the root store.RootStoreTypeWStrSpecifies or returns the type of the root store.SetHStoreCASpecifies the handle of the CA store.SetHStoreMySpecifies the handle of the personal store.SetHStoreRequestSpecifies the handle of the request store.SetHStoreROOTSpecifies the handle of the root store. '
ms.assetid: '15e4368b-4199-415a-9c2c-2c1351b717e6'
title: Certificate Store Functions
---

# Certificate Store Functions

The Xenroll.dll library contains the following methods and properties that you can use to manage certificate stores.

| Functions                                                          | Description                                                                                                                                                                                          |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CAStoreFlags**](https://msdn.microsoft.com/library/windows/desktop/aa385526)                 | Specifies or returns flags that control access to the [*certification authority*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certification-authority-gly) (CA) store.<br/> |
| [**CAStoreNameWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385528)           | Specifies or returns the name of the CA store.<br/>                                                                                                                                            |
| [**CAStoreTypeWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385530)           | Specifies or returns the type of the store identified by the **CAStoreName** property.<br/>                                                                                                    |
| [**MyStoreFlags**](https://msdn.microsoft.com/library/windows/desktop/aa385644)                 | Specifies or returns a flag that determines the path of the personal store.<br/>                                                                                                               |
| [**MyStoreNameWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385647)           | Specifies or returns the name of the personal store.<br/>                                                                                                                                      |
| [**MyStoreTypeWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385651)           | Specifies or returns the type of the personal store.<br/>                                                                                                                                      |
| [**RequestStoreFlags**](https://msdn.microsoft.com/library/windows/desktop/aa385675)       | Specifies or returns a flag that determines the path of the request store.<br/>                                                                                                                |
| [**RequestStoreNameWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385680) | Specifies or returns the name of the request store.<br/>                                                                                                                                       |
| [**RequestStoreTypeWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385685) | Specifies or returns the type of the request store.<br/>                                                                                                                                       |
| [**RootStoreFlags**](https://msdn.microsoft.com/library/windows/desktop/aa385702)             | Specifies or returns a flag that determines the path of the root store.<br/>                                                                                                                   |
| [**RootStoreNameWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385761)       | Specifies or returns the name of the root store.<br/>                                                                                                                                          |
| [**RootStoreTypeWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385790)       | Specifies or returns the type of the root store.<br/>                                                                                                                                          |
| [**SetHStoreCA**](https://msdn.microsoft.com/library/windows/desktop/aa385799)                   | Specifies the handle of the CA store.<br/>                                                                                                                                                     |
| [**SetHStoreMy**](https://msdn.microsoft.com/library/windows/desktop/aa385802)                   | Specifies the handle of the personal store.<br/>                                                                                                                                               |
| [**SetHStoreRequest**](https://msdn.microsoft.com/library/windows/desktop/aa385803)         | Specifies the handle of the request store.<br/>                                                                                                                                                |
| [**SetHStoreROOT**](https://msdn.microsoft.com/library/windows/desktop/aa385804)               | Specifies the handle of the root store.<br/>                                                                                                                                                   |



 

CertEnroll.dll does not export functionality that enables you to specify or retrieve store property values or copy certificates to specific stores.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> </dl>

 

 




