---
description: A client-implemented interface that allows developers to supply their own credentials dynamically at run time to authenticate non-domain joined containers with Active Directory.
title: ICcgDomainAuthCredentials interface (ccgplugins.h)
ms.topic: reference
ms.date: 10/20/2020
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ICcgDomainAuthCredentials
api_type: 
- COM
api_location: 
- ccgplugins.dll
---

# ICcgDomainAuthCredentials interface

A client-implemented interface that allows developers to supply their own credentials dynamically at run time to authenticate non-domain joined containers with Active Directory. 

## Members

The **ICcgDomainAuthCredentials** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ICcgDomainAuthCredentials** also has these types of members:

-   [Methods](#methods)

### Methods

The **ICcgDomainAuthCredentials** interface has these methods.



| Method                                           | Description                                                                                               |
|:-------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| [**GetPasswordCredentials**](iccgdomainauthcredentials-getpasswordcredentials.md)               | Returns credentials to authenticate a non-domain joined container with Active Directory.<br/>                                                              |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2019 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>ccgplugins.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>ccgplugins.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ccgplugins.dll</dt> </dl> |
| IID<br/>                      | 6ecda518-2010-4437-8bc3-46e752b7b172<br/>          |



 

