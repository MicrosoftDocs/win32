---
title: PS\_RemoteAccessHealthLocal class
description: Server Provider for getting health of Remote Access cluster, server (DA and VPN) and its components.
audience: developer
ms.assetid: '061c07d8-af20-4834-bf66-e7c3b60be475'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_RemoteAccessHealthLocal class", "PS_RemoteAccessHealthLocal class, described"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessHealthLocal
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
---

# PS\_RemoteAccessHealthLocal class

Server Provider for getting health of Remote Access cluster, server (DA and VPN) and its components.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class PS_RemoteAccessHealthLocal
{
};
```

## Members

The **PS\_RemoteAccessHealthLocal** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessHealthLocal** class has these methods.



| Method                                        | Description                                                                               |
|:----------------------------------------------|:------------------------------------------------------------------------------------------|
| [**Get**](get-ps-remoteaccesshealthlocal.md) | This cmdlet is used to obtain the current health of a Remote Access deployment<br/> |



 

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





