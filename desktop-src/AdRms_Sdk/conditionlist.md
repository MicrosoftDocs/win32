---
Description: Specifies the terms and conditions for using an Active Directory Rights Management Services (AD RMS) license or certificate. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 90c7c689-50d3-4b6d-80d0-abb7a6891b4e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: CONDITIONLIST
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CONDITIONLIST

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Specifies the terms and conditions for using an Active Directory Rights Management Services (AD RMS) license or certificate. This element has the following definition.

``` syntax
<!ELEMENT CONDITIONLIST (DESCRIPTION?,
                         %conditions;,
                         WATERMARK?)>
<!-- Conditions Entity -->
<!-- Conditions for exercising rights or using a license
  maxcount   - number of times you can use
  time       - when you can use
  access     - under what conditions you can use
  fee        - fees charged for use
  territory  - location at which use can occur
  track      - where and how to track usage
  refresh    - where and how often validity is to be refreshed
  condition  - generic condition other than the preceding
-->
<!ENTITY % conditions "( 
     MAXCOUNT  |
     TIME      |        
     ACCESS    | 
     FEE       |
     TERRITORY |
     TRACK     | 
     REFRESH   |
     CONDITION  )+">

<!ELEMENT MAXCOUNT (EVERY?)>
<!ATTLIST MAXCOUNT
  value CDATA #REQUIRED
  id CDATA #IMPLIED>

<!ELEMENT TIME (RANGETIME | INTERVALTIME | METEREDTIME)>
<!ATTLIST TIME
  id CDATA #IMPLIED>

<!ELEMENT ACCESS (PRINCIPAL*,
                  SECURITYLEVEL*,
                  SOURCE?,
                  DESTINATION?,
                  ANYONE*,
                  EVERYONE?)>
<!ATTLIST ACCESS
```

## Remarks

The **CONDITIONLIST** element is typically used when specifying content rights, and the most common encapsulated elements used to specify conditions are the **ACCESS** and **TIME** elements as shown in the following example.

## Examples


```XML
<RIGHTSGROUP name="Main-Rights">
  <RIGHTSLIST>
    <EDIT>
      <CONDITIONLIST>
        <ACCESS>
          <PRINCIPAL internal-id="1">
            <ENABLINGBITS type="sealed-key">
              <VALUE encoding="base64" size="1536">...</VALUE> 
            </ENABLINGBITS>
          </PRINCIPAL>
        </ACCESS>
        <TIME>
          <INTERVALTIME days="30"/> 
        </TIME>
      </CONDITIONLIST>
    </EDIT>
  </RIGHTSLIST>
</RIGHTSGROUP>
```



## Requirements



|                    |                                                           |
|--------------------|-----------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 or later<br/> |



## See also

<dl> <dt>

[**BODY**](body.md)
</dt> <dt>

[XrML Elements](xrml-elements.md)
</dt> </dl>

 

 




