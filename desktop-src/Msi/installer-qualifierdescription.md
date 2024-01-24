---
description: The read-only QualifierDescription property returns a text string describing the qualified component.
ms.assetid: 43615bd9-824b-4b84-a8f2-eef30cc7619a
title: Installer.QualifierDescription property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.QualifierDescription
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.QualifierDescription property

The read-only **QualifierDescription** property returns a text string describing the qualified component. This localizable string is authored into the AppData column of the [PublishComponent table](publishcomponent-table.md) and can be displayed to the user. The qualifier distinguishes multiple forms of the same component, such as a component that is implemented in multiple languages.

This property is read-only.

## Syntax


```JScript
propVal = Installer.QualifierDescription
```



## Property value

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiEnumComponentQualifiers**](/windows/desktop/api/Msi/nf-msi-msienumcomponentqualifiersa)
</dt> <dt>

[Qualified Components](qualified-components.md)
</dt> </dl>

 

 




