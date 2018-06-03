---
Description: Client and server licensor certificates and end-user licenses use the eXtensible rights Markup Language (XrML) version 1.2 RIGHTSLIST element to specify the rights they grant to a user.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e702155d-f5f9-4a34-93ed-f82b5a9daee9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Rights
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Rights

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Client and server licensor certificates and end-user licenses use the eXtensible rights Markup Language (XrML) version 1.2 [RIGHTSLIST](rightslist.md) element to specify the rights they grant to a user. Licensor certificates contain only the issue right. End user licenses can include multiple rights.

The following example shows a **RIGHTSLIST** element for a server licensor certificate. The ISSUE right contains a **CONDITIONLIST** element which in turn contains an **ACCESS** condition that specifies the principal **ID** and a **TIME** condition that specifies the time period during which the principal can issue issuance licenses.


```XML
<RIGHTSGROUP name="Main-Rights">
  <RIGHTSLIST>
    <RIGHT name="ISSUE">
      <CONDITIONLIST>
        <ACCESS>
          <PRINCIPAL internal-id="1">
            <ENABLINGBITS type="sealed- key">
              <VALUE encoding="base64" size="2560">
                   43g3IPo9Qv9YCutZ
                   tTP8zTk+S0t7jCvnibhivl04ecwpp9Up/X0KwjCU+E
                   Efd+JvrBo3piLasy3bY2aIV/v+vryiXeLHkLJZbJD4E
                   YvQHvic6PZIOMEGs8PltbROuMxNkRwmYlBmkQl4
                   oCFW7B08a0QNNYIkX7G9N1L0A5z6AhjnvOYALyp
                   K3+lpQ33dE3SmJTOaOPGqHXRTXXeqA4mq/hEHPK
                   2E8iPv8xPP01QyJxpkUtyW2TdzCyz7x25yVYofviuw
                   Gs3hMW7lkIiMGVnxG7Wpt+nD83YWm=
              </VALUE>
            </ENABLINGBITS>
          </PRINCIPAL>
        </ACCESS>
        <TIME>
          <RANGETIME>
            <FROM>2008-01-01T00:00</FROM>
            <UNTIL>2009-01-01T00:00</UNTIL>
          </RANGETIME>
        </TIME>
      </CONDITIONLIST>
    </RIGHT>
  </RIGHTSLIST>
</RIGHTSGROUP>
```



[*End-user licenses*](https://www.bing.com/search?q=*End-user licenses*) also use the **RIGHTSLIST** element but can include multiple predefined and custom rights for publishing and consuming content. The following rights are typical.

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



 

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> </dl>

 

 



