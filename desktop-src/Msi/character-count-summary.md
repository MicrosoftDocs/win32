---
Description: The Character Count Summary property is only used in transforms.
ms.assetid: d26d24a5-558e-4333-ae39-ffba1bbc5247
title: Character Count Summary property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Character Count Summary property

The **Character Count Summary** property is only used in transforms. This part of the summary information stream is divided into two 16-bit words. The upper word contains the [*transform validation flags*](t-gly.md#-msi-transform-validation-flags-gly). The lower word contains the [*transform error condition flags*](t-gly.md#-msi-transform-error-condition-flags-gly).

This property should be Null in an installation package or patch package.

## Requirements



|                    |                                                                                                                                                                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP.<br/> |



## See also

<dl> <dt>

[Summary Property Descriptions](summary-property-descriptions.md)
</dt> </dl>

 

 




