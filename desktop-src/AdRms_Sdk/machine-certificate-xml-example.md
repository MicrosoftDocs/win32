---
Description: The following example shows an XrML machine certificate. To see an actual machine certificate, activate the computer, navigate to the appropriate Machine Certificate Store, and open the CERT-Machine.drm file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1a402c85-1355-46b8-ac5c-8f5937c4ec22
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Machine Certificate XML Example
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Machine Certificate XML Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows an XrML machine certificate. To see an actual machine certificate, activate the computer, navigate to the appropriate [Machine Certificate Store](machine-certificate-store.md), and open the CERT-Machine.drm file.


```XML
- <XrML version="1.2" xmlns="">
  - <BODY type="LICENSE" version="3.0">
      <ISSUEDTIME>2008-03-17T15:49</ISSUEDTIME> 
    - <DESCRIPTOR>
    - <OBJECT type="Machine-Certificate">
        <ID type="MS-GUID">
          {958E4BE1-6B28-4C3D-9DEC-EA5B36169085}\
        </ID> 
        <NAME>Microsoft Machine-Certificate</NAME> 
      </OBJECT>
      </DESCRIPTOR>
    - <ISSUER>
      - <OBJECT type="MS-DRM-Desktop-Security-Processor">
          <ID type="MS-GUID">
            {d250be5b-50f1-48e6-81a5-6003ccf9cb44}
          </ID> 
          <NAME>
             Microsoft DRM ISV Desktop Security Processor 
             Activation Certificate
           </NAME> 
        </OBJECT>
      - <PUBLICKEY>
          <ALGORITHM>RSA</ALGORITHM> 
        - <PARAMETER name="public-exponent">
            <VALUE encoding="integer32">65537</VALUE> 
          </PARAMETER>
        - <PARAMETER name="modulus">
            <VALUE encoding="base64" size="1024">
              z9738mlRsvk7jRuUMUMe89JWYVVeF6MwjilbtTFgMyIvU6lbbbOjbgT3
              3vzLRA8opv4u6YzK30dlFzzN3UwKX4LqKmUr7kbg0bUtMM3UK0UvfnWX
              +ucPVR8K7cRX/g9ZOh+MgNllKfsmQv5nG48w0I0q/cpmDlYrqwBGGAD8
              isk=
            </VALUE> 
          </PARAMETER>
        </PUBLICKEY>
      </ISSUER>
    - <DISTRIBUTIONPOINT>
      - <OBJECT type="Activation">
          <ID type="MS-GUID">
            {99F48562-703E-4E7D-9175-DD69C66921B7}
          </ID> 
          <NAME>Microsoft Activation</NAME> 
          <ADDRESS type="URL">file:///rmactivate.exe</ADDRESS> 
        </OBJECT>
      </DISTRIBUTIONPOINT>
    - <ISSUEDPRINCIPALS>
      - <PRINCIPAL>
        - <OBJECT type="Machine-Unique-Identifier">
            <ID type="MS-GUID">
              {8a0acfdb-b60f-49bd-a781-f6b41e876219}
            </ID> 
            <NAME>Machine</NAME> 
          </OBJECT>
        - <PUBLICKEY>
            <ALGORITHM>RSA</ALGORITHM> 
          - <PARAMETER name="public-exponent">
              <VALUE encoding="integer32">65537</VALUE> 
            </PARAMETER>
          - <PARAMETER name="modulus">
              <VALUE encoding="base64" size="1024">
                2Q7nZtumLn6yIlt2xYpaNAi8Ffgk0yKOXOZXAJ423SnhkAl9Ge2WOw
                adHYTqT9wtX9dc9WTA32MU+4jcTgO4qouMvKHwBF9vXI1v37tY0bqY
                KrrCz3QmtDhDSwt8RZvoBVavh2nAggv3XeEA7RWRtG0DVXKjuOnyEN
                6iFzEzhbs=
              </VALUE> 
            </PARAMETER>
          </PUBLICKEY>
        - <DIGEST>
            <ALGORITHM>SHA1</ALGORITHM> 
          - <PARAMETER name="codingtype">
              <VALUE encoding="string">surface-coding</VALUE> 
            </PARAMETER>
            <VALUE encoding="base64" size="160">
              i8m+LJyoj+3ou1XLohjh+O+V0to=
            </VALUE> 
          </DIGEST>
          <SECURITYLEVEL name="Platform" value="2.6.0.6000"/> 
          <SECURITYLEVEL 
            name="Manufacturer" 
            value="Microsoft Corporation mcoregen DLL 6.0.5840.16389 
                  (RMS Client v2.0 Desktop Security Processor)"/> 
          <SECURITYLEVEL 
            name="Repository" 
            value="Microsoft Corporation Windows RMS Client v2.0 
                  secure repository 6.0.5840.16389"/> 
        </PRINCIPAL>
      </ISSUEDPRINCIPALS>
    </BODY>
  - <SIGNATURE>
    - <DIGEST>
        <ALGORITHM>SHA1</ALGORITHM> 
      - <PARAMETER name="codingtype">
          <VALUE encoding="string">surface-coding</VALUE> 
        </PARAMETER>
        <VALUE encoding="base64" size="160">
          HbcVyJiDVTCu+cymql4BY4BpjUA=
        </VALUE> 
      </DIGEST>
      <ALGORITHM>RSA PKCS#1-V1.5</ALGORITHM> 
      <VALUE encoding="base64" size="1024">
        TlPe5eNPl+89wF2prAmgcjs54hnnA/GQzUVds37UaTOlaMvs7CCnNmw+q5ui1q
        cFyYWSOpQW9FU4xt3aWn2oJIPfyuwuF2s+eQBxzX3l7PuGiTVTx6I09yK5mgyj
        AZDrS407znQzQ4VV9glsda1lhZYYLh8khDgwTVcn5AbjSQY=
      </VALUE> 
    </SIGNATURE>
  </XrML>
   .
   .
   .
- <XrML xmlns="" version="1.2">
- <XrML xmlns="" version="1.2">
```



## Related topics

<dl> <dt>

[Activating a Computer](activating-a-computer.md)
</dt> <dt>

[Machine Certificates](machine-certificates.md)
</dt> </dl>

 

 



