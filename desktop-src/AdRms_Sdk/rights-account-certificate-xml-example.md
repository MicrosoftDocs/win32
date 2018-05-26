---
Description: The following example shows an XrML rights account certificate (RAC) chain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4887578b-a3ba-45f1-84d6-ff3649457437
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Rights Account Certificate XML Example
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Rights Account Certificate XML Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows an XrML rights account certificate (RAC) chain. The RAC was issued to the user account someone@example.com. The name of the AD RMS server that issued the RAC was EXAMPLESRV2008. To see an actual RAC, activate the user, navigate to the appropriate [Rights Account Certificate Store](rights-account-certificate-store.md), and open the certificate file.

The file name format for a RAC in the Pre-production hierarchy is GIC-*user account*-*user ID GUID*.drm. For example, the following RAC was saved in the file named GIC-someone@example.com-{f39c5f0b;kb861;k460c;k8a21;kb8a0b9a9c568}.drm.


```XML
- <XrML xmlns="" version="1.2">
  - <BODY type="LICENSE" version="3.0">
      <ISSUEDTIME>2008-03-17T16:04</ISSUEDTIME> 
    - <VALIDITYTIME>
        <FROM>2008-03-16T16:04</FROM> 
        <UNTIL>2009-03-17T16:04</UNTIL> 
      </VALIDITYTIME>
    - <DESCRIPTOR>
      - <OBJECT type="Group-Identity-Credential">
          <ID type="MS-GUID">
            {f39c5f0b-b861-460c-8a21-b8a0b9a9c568}
          </ID> 
        </OBJECT>
      </DESCRIPTOR>
    - <ISSUER>
      - <OBJECT type="MS-DRM-Server">
          <ID type="MS-GUID">
            {e03ee46f-e62a-48d7-81f0-2d8d5d522c9d}
          </ID> 
          <NAME>EXAMPLESRV2008</NAME> 
          <ADDRESS type="URL">HTTP://example.com:80/_wmcs</ADDRESS> 
        </OBJECT>
      - <PUBLICKEY>
          <ALGORITHM>RSA</ALGORITHM> 
        - <PARAMETER name="public-exponent">
            <VALUE encoding="integer32">65537</VALUE> 
          </PARAMETER>
        - <PARAMETER name="modulus">
            <VALUE encoding="base64" size="1024">
              1fn3bqaD3kdFtl+uo1mc/PKPNZyIjJ+KN+EACM72bSZwswcUTc8u75H
              0rllk9bgonpFTt9MCdfl7f+NC2OuWv2rC9nuBKt6CN/wMEVpF+ByjkU
              zMTA1Ktu/ziS4BJ9L7t1bUWEqa3nWb1B6MV/M+jeNgjiRMpGi+vzn3s
              D/d8Oo=
            </VALUE> 
          </PARAMETER>
        </PUBLICKEY>
        <SECURITYLEVEL name="Server-Version" value="6.0.0.0"/> 
        <SECURITYLEVEL name="Server-SKU" value="RMS 2.0"/> 
      </ISSUER>
    - <DISTRIBUTIONPOINT>
      - <OBJECT type="Activation">
          <ID type="MS-GUID">
            {8BA9EA80-99E4-4a2b-9764-4CD84F77C3A0}
          </ID> 
          <NAME>Microsoft Identity Certification Server</NAME> 
          <ADDRESS type="URL">
            http://example.com/_wmcs/certification
          </ADDRESS> 
        </OBJECT>
      </DISTRIBUTIONPOINT>
    - <ISSUEDPRINCIPALS>
      - <PRINCIPAL internal-id="1">
        - <OBJECT type="Group-Identity">
            <ID type="Windows">
              S-1-5-21-1226287486-3652005974-3671177567-1114
            </ID> 
            <NAME>someone@example.com</NAME> 
          </OBJECT>
        - <PUBLICKEY>
            <ALGORITHM>RSA</ALGORITHM> 
          - <PARAMETER name="public-exponent">
              <VALUE encoding="integer32">65537</VALUE> 
            </PARAMETER>
          - <PARAMETER name="modulus">
              <VALUE encoding="base64" size="1024">
                raMBBHBY7UbNE0bHh1Mc2G2LjBQfI/x/scBACTAm6Y12K+xQlve3p
                NlcnFcuPrfguSpNrXq3bdk+zdONH92zzxSlwqvVXqubwNinLESusH
                snpcVPGkPLV3PqxZ/JHOiEWKoLPkigNHGfatrBbnofCqRQhiG6it7
                FbHvNMRAgxbE=
            </VALUE> 
            </PARAMETER>
          </PUBLICKEY>
          <SECURITYLEVEL 
            name="Group-Identity-Credential-Type" 
            value="Persistent"/> 
          <SECURITYLEVEL 
            name="Group-Identity-Policy" 
            value="Group-Identity-Credential"/> 
          <SECURITYLEVEL 
            name="Group-Identity-Type" 
            value="Group"/> 
        </PRINCIPAL>
    - </ISSUEDPRINCIPALS>
    - <FEDERATIONPRINCIPALS>
      - <PRINCIPAL>
        - <OBJECT type="Machine-Unique-Identifier">
            <ID type="MS-GUID">
              {8a0acfdb-b60f-49bd-a781-f6b41e876219}
            </ID> 
            <NAME>Machine</NAME> 
          </OBJECT>
        - <ENABLINGBITS type="sealed-key">
            <VALUE encoding="base64" size="6144">
              ox7jiE7iXtnP5Q4p/ZPfh4VAP5sFh/wI+8XsK94+KBO8yfwytsNCoUP
              JU3twWHoBNTIdbVCvSFFmhp+Uw71rHCB22Ud3ZUaV81a5ZjbsyFltiu
              FFUOeqOKUGXQwKHrVcb6Yi2rEOmimKoBr1S/SP99g5D3xEZjxslFI8q
              F3PblXdysVm8alF+KiLkWLO0B+doTd+7OnL48H1xQZnUFLVy2uBp+s5
              JJDLd1+38Oj/qjl992EhHZMvle567g+vRLQ4pabIrtZnIw/hAa0yBWP
              FlRNJ6v0qsj1FeM4mRiKYvGazyVDEYX+Js1sc1RUY4XNLo7tPlBt/4q
              JHHhuGhX2jltXRKTQprlofb/ZnTfme+rBNKX5Rzd3+fjp0dFjdllfMG
              Z5J+Z6PSwAAs9ojlner6j2kv88yHx700ZaTdCxhKPEVL9IyNPjFUHo/
              b+499DIPu7tp2E3DlEEusnsnwZqIehpt8tghLzfUMM2YJe3T1poKVF0
              SWjVfr2OKRZ3qQPdI+/3/cQzaGirgvRDuifJGduzLqZ2uABKwqYv2zP
              ELKOKPuDWqckhgj83n/EYtyM/beCz0ZmEGHdAEmXFHr701t7heGI9aQ
              jUwNjWmpwMUKTgKGfA0dNq4cJk1p/VO1+b2TS3yAC2jtwA5ZaejrQ8g
              2H/S2D82ht8A9tGUjDfoqn4T2RN1laLXGwbzAto31I4kUWpcziakJ+/
              XNBH4F961d6177Sie1IkGiLGnMSM3nmpdQPjad/z8YS3fPcE+LkbaP8
              vmXZl4GY6nNSvkvTT/nxhFfn/Fm17HFvjovBhSB6NOFzkSiuXDcPXlU
              X/BTGZk0p8j4yXQNtO9b3H+OtGEuwqnD8S69tIrpH+jpl/VCFXFKp3M
              rcVUZfjhBGfZHapCul5dZfir32dU6bkTD/FmSbSVClr5rO7/sZ/Wlvl
              lv4mw/gg642EnvzURDMFFZb+XYALFGdvMt3kZevK4o5hCE0yEP2PtAb
              fWv1jpseo3nNRC/mMsv8nXgcdW1MKbuKEH
            </VALUE> 
          </ENABLINGBITS>
          <SECURITYLEVEL 
            name="Manufacturer" 
            value=
              "Microsoft Corporation mcoregen DLL 6.0.5840.16389 (RMS 
              Client v2.0 Desktop Security Processor)"/> 
          <SECURITYLEVEL 
            name="Platform" 
            value="2.6.0.6000"/> 
          <SECURITYLEVE 
            name="Repository" 
            value=
              "Microsoft Corporation Windows RMS Client v2.0 secure 
              repository 6.0.5840.16389"/> 
        </PRINCIPAL>
      </FEDERATIONPRINCIPALS>
    </BODY>
  - <SIGNATURE>
      <DIGEST>
        <ALGORITHM>SHA1</ALGORITHM> 
      - <PARAMETER name="codingtype">
          <VALUE encoding="string">surface-coding</VALUE> 
        </PARAMETER>
        <VALUE encoding="base64" size="160">
          Xc+84uqrehgkwjwHGAedTv7UeK0=
        </VALUE> 
      </DIGEST>
    - <ALGORITHM>RSA PKCS#1-V1.5</ALGORITHM> 
        <VALUE encoding="base64" size="1024">
          SaZvQJOL9D478f5sxLq3Jdn5ZB11oHvfKr8xa3oPI5xwmFnnsol+rTJKWYP
          K0lyfRhpqobgQmqtx9HaVGp/kK5HcPoMFVp8RRnbKogZDZVX3lKMq+vJeJb
          RIassz6TZQICTBcf0QL/ba3qVNYGP3kl3LyRAK/DaHsD1w5XXAfmk=
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

[Activating a User](activating-a-user.md)
</dt> <dt>

[Rights Account Certificates](rights-account-certificates.md)
</dt> </dl>

 

 



