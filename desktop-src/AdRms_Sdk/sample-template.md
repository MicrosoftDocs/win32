---
Description: The following XrML example shows a sample official rights template.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8d7fabe2-5ed2-4987-98e3-b09e94cd5831
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Sample Template
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sample Template

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following XrML example shows a sample official rights template.


```XML
<?xml version="1.0" ?> 
  <XrML xmlns="" version="1.2">
    <BODY type="Microsoft Official Rights Template">
      <ISSUEDTIME>2007-07-12T20:41</ISSUEDTIME> 
      <DESCRIPTOR>
        <OBJECT>
          <ID type="MS-GUID">
            {78862306-1fb3-4251-b83d-143db199f5d5}
          </ID> 
          <NAME>
            LCID 1033:NAME Contoso Confidential:
            DESCRIPTION Generic Contoso Template for all employees;
          </NAME> 
        </OBJECT>
      </DESCRIPTOR>
      <ISSUER>
        <OBJECT type="MS-DRM-Server">
          <ID type="MS-GUID">
            {72049fbf-db1a-4122-bb9b-4197029a58e5}
          </ID> 
          <ADDRESS type="URL">
            http://rmcontoso/_wmcs
          </ADDRESS> 
        </OBJECT>
        <PUBLICKEY>
          <ALGORITHM>RSA</ALGORITHM> 
          <PARAMETER name="public-exponent">
            <VALUE encoding="integer32">65537</VALUE> 
          </PARAMETER>
          <PARAMETER name="modulus">
            <VALUE encoding="base64" size="1024">
              VRK+j5k+FqtBhdARLYE9nIgyscwt7euR6MdVeFbpT51RaVsI6abDZI
              OGRNuS/dLa5usMoW+iX6qW5qM+smQaFkRt2gMezynSv/e8xRoY/JSa
              tvgU0JDtNFUX67VY10rsXh8tgyNg/+ZEJih3V0Iq702lOW0Sx8plIp
              IiKx0a1tc=
            </VALUE> 
          </PARAMETER>
        </PUBLICKEY>
      </ISSUER>
      <DISTRIBUTIONPOINT>
        <OBJECT type="Publishing-URL">
          <ID type="MS-GUID">
            {9A23D98E-4449-4ba5-812A-F30808F3CB16}
          </ID> 
          <NAME>Publishing Point</NAME> 
          <ADDRESS type="URL">
            http://rmcontoso/_wmcs/licensing
          </ADDRESS> 
        </OBJECT>
      </DISTRIBUTIONPOINT>
      <DISTRIBUTIONPOINT>
        <OBJECT type="Referral-Info">
          <ID type="MS-GUID">
            {D5BA4021-27D6-42C0-A322-4064E2F91AB0}
          </ID> 
          <ADDRESS type="URL">
            johndoe@contoso.com
          </ADDRESS> 
        </OBJECT>
      </DISTRIBUTIONPOINT>
      <WORK>
      <OBJECT>
        <ID type=""/> 
      </OBJECT>
      <PRECONDITIONLIST>
        <TIME>
          <RANGETIME>
            <FROM>2007-07-12T20:41</FROM> 
            <UNTIL>2008-05-16T00:00</UNTIL> 
          </RANGETIME>
        </TIME>
      </PRECONDITIONLIST>
      <CONDITIONLIST>
        <REFRESH>
          <DISTRIBUTIONPOINT>
            <OBJECT type="Revocation">
              <ID type="ascii-tag">
                External revocation authority
              </ID> 
              <NAME>Revocation Point</NAME> 
              <ADDRESS type="URL">
                http://rmcontoso/revocation/myrevocation.xml
              </ADDRESS> 
            </OBJECT>
         </DISTRIBUTIONPOINT>
         <INTERVALTIME days="10"/> 
       </REFRESH>
     </CONDITIONLIST>
     <RIGHTSGROUP name="Main-Rights">
       <RIGHTSLIST>
         <RIGHT name="OWNER">
           <CONDITIONLIST>
             <ACCESS>
               <PRINCIPAL>
                 <OBJECT>
                   <ID type="Internal">Owner</ID> 
                 </OBJECT>
               </PRINCIPAL>
             </ACCESS>
           </CONDITIONLIST>
         </RIGHT>
         <VIEW>
           <CONDITIONLIST>
             <ACCESS>
               <PRINCIPAL>
                 <OBJECT>
                   <ID type="Unspecified"/> 
                   <NAME>contoso-fte@contoso.com</NAME> 
                 </OBJECT>
               </PRINCIPAL>
             </ACCESS>
           </CONDITIONLIST>
         </VIEW>
       <RIGHT name="REPLY">
         <CONDITIONLIST>
           <ACCESS>
             <PRINCIPAL>
               <OBJECT>
                 <ID type="Unspecified"/> 
                 <NAME>contoso-fte@contoso.com</NAME> 
               </OBJECT>
             </PRINCIPAL>
           </ACCESS>
         </CONDITIONLIST>
       </RIGHT>
       <RIGHT name="REPLYALL">
         <CONDITIONLIST>
           <ACCESS>
             <PRINCIPAL>
               <OBJECT>
                 <ID type="Unspecified"/> 
                 <NAME>contoso-fte@contoso.com</NAME> 
               </OBJECT>
             </PRINCIPAL>
           </ACCESS>
         </CONDITIONLIST>
       </RIGHT>
     </RIGHTSLIST>
  </RIGHTSGROUP>
  </WORK>
  <AUTHENTICATEDDATA name="VIEWER" id="APPSPECIFIC">
    1
  </AUTHENTICATEDDATA> 
  <AUTHENTICATEDDATA name="NOLICCACHE" id="APPSPECIFIC">
    1
  </AUTHENTICATEDDATA> 
  <AUTHENTICATEDDATA name="AppVersion" id="APPSPECIFIC">
    1.0.0.1
  </AUTHENTICATEDDATA> 
  </BODY>
  <SIGNATURE>
    <DIGEST>
      <ALGORITHM>SHA1</ALGORITHM> 
      <PARAMETER name="codingtype">
        <VALUE encoding="string">
          surface-coding
        </VALUE> 
      </PARAMETER>
      <VALUE encoding="base64" size="160">
        jn1MSweIo+LHJQb8/karbhw2R40=
      </VALUE> 
    </DIGEST>
    <ALGORITHM>RSA PKCS#1-V1.5</ALGORITHM> 
    <VALUE encoding="base64" size="1024">
      WD1l1Vf45kXyotc5+TH+bCWXIbCIU4/qrfKuLRH1TPsvimk5XWewtwDBTfjHi6
      jIDZtfoViWm40sJoXWgr02xDEynHIw62nfa3UYwgUVLvPFOASLjii5SdrwF5aB
      UR7a3UHiV51c/kJ2Wl6H1830zqyAbGFziD7ns3C1w97V3TI=
    </VALUE> 
  </SIGNATURE>
</XrML>
```



## Related topics

<dl> <dt>

[Official Template XrML](official-template-xrml.md)
</dt> <dt>

[Working with Licenses and Templates](working-with-licenses-and-templates.md)
</dt> </dl>

 

 



