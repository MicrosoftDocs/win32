---
Description: Specifies the type of data encryption to use to connect to a wireless LAN.
ms.assetid: 0ba24106-bd6f-465a-af80-ce85501756b9
title: encryption (authEncryption) Element
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# encryption (authEncryption) Element

The encryption (authEncryption) element specifies the type of data encryption to use to connect to a wireless LAN.

``` syntax
<xs:element name="encryption">
    <xs:simpleType>
        <xs:restriction
            base="string"
        >
            <xs:enumeration
                value="none"
             />
            <xs:enumeration
                value="WEP"
             />
            <xs:enumeration
                value="TKIP"
             />
            <xs:enumeration
                value="AES"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The element is defined by the [**authEncryption**](wlan-profileschema-authencryption-security-element.md) element.

## Remarks

When the **encryption** element has a value of WEP, [**keyType**](wlan-profileschema-keytype-sharedkey-element.md) must be set to **networkKey**.

The AES encryption method is as specified in the [802.1X](http://go.microsoft.com/fwlink/p/?linkid=89910) and [802.11i](http://go.microsoft.com/fwlink/p/?linkid=89906) specifications.

## Examples

To view sample profiles that use the **encryption** element, see [Wireless Profile Samples](wireless-profile-samples.md).

## Requirements



|                                     |                                                                     |
|-------------------------------------|---------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                 |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**authEncryption**](wlan-profileschema-authencryption-security-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**authEncryption (security)**](wlan-profileschema-authencryption-security-element.md)
</dt> </dl>

 

 




