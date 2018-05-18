---
Description: 'The installer sets the ProductState property to the installation state for the product at initialization.'
ms.assetid: 'f26f3229-d1ce-4802-99b1-857c6501c828'
title: ProductState property
---

# ProductState property

The installer sets the **ProductState** property to the installation state for the product at initialization. This property is set to one of the following INSTALLSTATE data types returned by [**MsiQueryProductState**](msiqueryproductstate.md).



| INSTALLSTATE             | Numeric value | Installation state of product                   |
|--------------------------|---------------|-------------------------------------------------|
| INSTALLSTATE\_UNKNOWN    | -1            | The product is neither advertised or installed. |
| INSTALLSTATE\_ADVERTISED | 1             | The product is advertised but not installed.    |
| INSTALLSTATE\_ABSENT     | 2             | The product is installed for a different user.  |
| INSTALLSTATE\_DEFAULT    | 5             | The product is installed for the current user.  |



 

## Requirements



|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




