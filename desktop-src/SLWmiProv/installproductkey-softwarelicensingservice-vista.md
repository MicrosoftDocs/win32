---
Description: Not supported. Installs a product key for the current product.
ms.assetid: e3bab173-4fee-48d0-8cff-35499b22ae54
title: InstallProductKey method of the SoftwareLicensingService class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InstallProductKey method of the SoftwareLicensingService class

Not supported. Installs a product key for the current product.

**Windows Vista and Windows Server 2008:** Use the Windows 7 version of the [**InstallProductKey**](https://msdn.microsoft.com/library/cc534590) method.

## Syntax


```mof
unit32 InstallProductKey(
  [in] string ProductKey
);
```



## Parameters

<dl> <dt>

*ProductKey* \[in\]
</dt> <dd>

Specifies the product key to install.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| End of client support<br/>    | Windows Vista<br/>                                                             |
| End of server support<br/>    | Windows Server 2008<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>SLWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SLWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SoftwareLicensingService**](softwarelicensingservice-vista.md)
</dt> </dl>

 

 




