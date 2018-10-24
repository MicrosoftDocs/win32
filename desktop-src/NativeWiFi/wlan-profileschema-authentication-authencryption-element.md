---
Description: Specifies the authentication method to be used to connect to the wireless LAN.
ms.assetid: fb6c5cce-05d6-41a2-acf4-9ae2713079dd
title: authentication (authEncryption) Element
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- authentication
api_type: 
- Schema
api_location: 
---

# authentication (authEncryption) Element

The authentication (authEncryption) element specifies the authentication method to be used to connect to the wireless LAN.

``` syntax
<xs:element name="authentication">
    <xs:simpleType>
        <xs:restriction
            base="string"
        >
            <xs:enumeration
                value="open"
             />
            <xs:enumeration
                value="shared"
             />
            <xs:enumeration
                value="WPA"
             />
            <xs:enumeration
                value="WPAPSK"
             />
            <xs:enumeration
                value="WPA2"
             />
            <xs:enumeration
                value="WPA2PSK"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The element is defined by the [**authEncryption**](wlan-profileschema-authencryption-security-element.md) element.

## Remarks

The following table describes the enumeration values.



| Value   | Description                            |
|---------|----------------------------------------|
| open    | Open 802.11 authentication.            |
| shared  | Shared 802.11 authentication.          |
| WPA     | WPA-Enterprise 802.11 authentication.  |
| WPAPSK  | WPA-Personal 802.11 authentication.    |
| WPA2    | WPA2-Enterprise 802.11 authentication. |
| WPA2PSK | WPA2-Personal 802.11 authentication.   |



 

For more information about 802.11 authentication methods, see the [WPA](http://go.microsoft.com/fwlink/p/?linkid=391356), [802.1X](http://go.microsoft.com/fwlink/p/?linkid=89910), and [802.11i](http://go.microsoft.com/fwlink/p/?linkid=89906) specifications.

## Examples

To view sample profiles that use the **authentication** element, see [Wireless Profile Samples](wireless-profile-samples.md).

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

 

 




