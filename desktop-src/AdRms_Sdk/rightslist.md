---
Description: Specifies a collection of rights for a RIGHTSGROUP element. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 57e75ebf-4120-47b2-9d14-4544afeac638
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RIGHTSLIST
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RIGHTSLIST

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Specifies a collection of rights for a **RIGHTSGROUP** element. This element has the following definition.

``` syntax
<!-- Individual rights -->
<!ELEMENT RIGHTSLIST (RIGHT | SELL | COPY | LOAN | 
                      TRANSFER | RETURN | PLAY | PRINT |
                      VIEW | EXPORT | EDIT | EXTRACT | EMBED |
                      BACKUP | RESTORE | VERIFY | FOLDER | DIRECTORY |
                      DELETE | INSTALL | UNINSTALL)+>

<!-- Generic Right -->
<!ELEMENT RIGHT (DESCRIPTION?,
                 SECURESTORE?,
                 PRECONDITIONLIST?,
                 CONDITIONLIST?,
                 NEXTRIGHTS?,
                 PLAYER?,
                 SOURCE?,
                 DESTINATION?,
                 PARAMETER*)>
<!ATTLIST RIGHT
  name CDATA #REQUIRED
  type CDATA #IMPLIED
  id CDATA #IMPLIED>

<!-- Print Right -->
<!ELEMENT PRINT (PRINTER?,
                 DESCRIPTION?,
                 SECURESTORE?,
                 PRECONDITIONLIST?,
                 CONDITIONLIST?,
                 PARAMETER*)>
<!ATTLIST PRINT
  id CDATA #IMPLIED>

<!-- View Right -->
<!ELEMENT VIEW (VIEWER?,
                DESCRIPTION?,
                SECURESTORE?,
                PRECONDITIONLIST?,
                CONDITIONLIST?,
                PARAMETER*)>
<!ATTLIST VIEW
  id CDATA #IMPLIED>

<!-- Export Right -->
<!ELEMENT EXPORT (REPOSITORY?,
                  DESCRIPTION?,
                  SECURESTORE?,
                  PRECONDITIONLIST?,
                  CONDITIONLIST?,
                  PARAMETER*)>
<!ATTLIST EXPORT
  id CDATA #IMPLIED>

<!-- Edit Right -->
<!ELEMENT EDIT (EDITOR?,
                DESCRIPTION?,
                SECURESTORE?,
                PRECONDITIONLIST?,
                CONDITIONLIST?,
                NEXTRIGHTS?)>
<!ATTLIST EDIT
  id CDATA #IMPLIED>

<!-- Extract Right -->
<!ELEMENT EXTRACT (EDITOR?,
                   DESCRIPTION?,
                   SECURESTORE?,
                   PRECONDITIONLIST?,
                   CONDITIONLIST?,
                   NEXTRIGHTS?)>
<!ATTLIST EXTRACT
  id CDATA #IMPLIED>
```

## Remarks

The predefined rights typically used in an Active Directory Rights Management Services (AD RMS) license, such as **VIEW** and **PRINT**, are listed below the **RIGHTSLIST** element in the preceding definition. AD RMS also uses the **RIGHT** element to define custom rights. The meanings of the rights typically used in AD RMS are defined in the following table.



| Right          | Type       | Meaning                                                                                                                                      |
|----------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| DOCEDIT        | Custom     | Edit the content.                                                                                                                            |
| EDIT           | Predefined | Save the content.                                                                                                                            |
| EXPORT         | Predefined | Save the content under a different file name (Save As). Note that, depending on the application, the file might be saved without protection. |
| EXTRACT        | Predefined | Extract the unencrypted content.                                                                                                             |
| FORWARD        | Custom     | Forward the content.                                                                                                                         |
| OWNER          | Custom     | Grant full control.                                                                                                                          |
| PRINT          | Predefined | Print the content.                                                                                                                           |
| REPLY          | Custom     | Reply to the sender.                                                                                                                         |
| REPLYALL       | Custom     | Reply to all parties listed.                                                                                                                 |
| VIEW           | Predefined | View the content.                                                                                                                            |
| VIEWRIGHTSDATA | Custom     | View the available rights.                                                                                                                   |



 

## Examples

The following example shows a **RIGHTSLIST** element that contains a single **EDIT** right. The right contains a [**CONDITIONLIST**](conditionlist.md) that stipulates limits on that right.


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

[**WORK**](work.md)
</dt> </dl>

 

 




