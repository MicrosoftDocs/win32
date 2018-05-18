---
title: SupportedOSVersion Complex Type
description: Specifies the minimum operating system version on which the troubleshooting pack can run.
ms.assetid: '778e8d52-e317-4077-adca-b03abe685775'
keywords: ["SupportedOSVersion complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- SupportedOSVersion
api_type:
- Schema
---

# SupportedOSVersion Complex Type

Specifies the minimum operating system version on which the troubleshooting pack can run.

``` syntax
<xs:complexType name="SupportedOSVersion">
    <xs:simpleContent>
        <xs:extension
            base="Version"
        >
            <xs:attribute name="clientSupported"
                type="xs:boolean"
                use="required"
             />
            <xs:attribute name="serverSupported"
                type="xs:boolean"
                use="required"
             />
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>
```

## Attributes



| Name            | Type       | Description                                                                  |
|-----------------|------------|------------------------------------------------------------------------------|
| clientSupported | xs:boolean | Specify true if the pack can run on the client; otherwise, false.<br/> |
| serverSupported | xs:boolean | Specify true if the pack can run on the server; otherwise, false.<br/> |



## Remarks

For a list of supported operating system version numbers, see the Remarks section of the [**OSVERSIONINFO**](https://msdn.microsoft.com/library/windows/desktop/ms724834) structure.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SupportedOSVersion (GlobalDiagnosticPackage) Element**](package-supportedosversion-globaldiagnosticpackage-element.md)
</dt> <dt>

[**SupportedOSVersion (LocalDiagnosticPackage) Element**](package-supportedosversion-localdiagnosticpackage-element.md)
</dt> </dl>

 

 





