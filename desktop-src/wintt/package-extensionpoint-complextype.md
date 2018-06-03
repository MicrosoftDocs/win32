---
title: ExtensionPoint Complex Type
description: Contains well-formed XML that extends the feature in which it is used.
ms.assetid: a421ec5d-4a1c-4c82-90be-f2896fcd907e
keywords:
- ExtensionPoint complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- ExtensionPoint
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ExtensionPoint Complex Type

Contains well-formed XML that extends the feature in which it is used.

``` syntax
<xs:complexType name="ExtensionPoint">
    <xs:sequence>
        <xs:any
            processContents="lax"
            minOccurs="0"
            maxOccurs="unbounded"
            namespace="##any"
         />
    </xs:sequence>
</xs:complexType>
```

## Remarks

The XML that you specify depends on the context in which it is used. For valid XML that you can specify, see the parent element to which the extension point belongs.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**ExtensionPoint (Choice) Element**](package-extensionpoint-choice-element.md)
</dt> <dt>

[**ExtensionPoint (GlobalDiagnosticPackage) Element**](package-extensionpoint-globaldiagnosticpackage-element.md)
</dt> <dt>

[**ExtensionPoint (GlobalRootcause) Element**](package-extensionpoint-globalrootcause-element.md)
</dt> <dt>

[**ExtensionPoint (LaunchUIInteraction) Element**](package-extensionpoint-launchuiinteraction-element.md)
</dt> <dt>

[**ExtensionPoint (MultipleResponseInteraction) Element**](package-extensionpoint-multipleresponseinteraction-element.md)
</dt> <dt>

[**ExtensionPoint (PauseInteraction) Element**](package-extensionpoint-pauseinteraction-element.md)
</dt> <dt>

[**ExtensionPoint (SingleResponseInteraction) Element**](package-extensionpoint-singleresponseinteraction-element.md)
</dt> <dt>

[**ExtensionPoint (TextInteraction) Element**](package-extensionpoint-textinteraction-element.md)
</dt> <dt>

[**ExtensionPoint (LocalDiagnosticPackage) Element**](package-extensionpoint-localdiagnosticpackage-element.md)
</dt> <dt>

[**ExtensionPoint (LocalRootcause) Element**](package-extensionpoint-localrootcause-element.md)
</dt> <dt>

[**ExtensionPoint (Resolver) Element**](package-extensionpoint-resolver-element.md)
</dt> <dt>

[**ExtensionPoint (Script) Element**](package-extensionpoint-script-element.md)
</dt> <dt>

[**ExtensionPoint (Troubleshooter) Element**](package-extensionpoint-troubleshooter-element.md)
</dt> <dt>

[**ExtensionPoint (Verifier) Element**](package-extensionpoint-verifier-element.md)
</dt> </dl>

 

 





