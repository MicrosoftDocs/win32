---
Description: Peer identity and group configuration files can be imported and exported from one endpoint to another by using the identity import and export functions located in the Identity Manager and Grouping APIs.
ms.assetid: 876d9c57-15f6-4f5e-8035-792e15f8035e
title: Identity and Group Configuration Import and Export
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Identity and Group Configuration Import and Export

Peer identity and group configuration files can be imported and exported from one endpoint to another by using the identity import and export functions located in the Identity Manager and Grouping APIs. These functions are useful because they allow a user to quickly and conveniently export identities and group configuration information from one computer to another computer.

## Importing and Exporting Peer Identity Data

The identity data of a peer is exported by calling [**PeerIdentityExport**](/windows/win32/P2P/nf-p2p-peeridentityexport?branch=master) with the identity name to export and a password used to encrypt the associated credentials. This function returns an XML string that contains the identity name of the peer and the encrypted credentials for that specific identity, which can then be passed to a different computer by using an external transfer mechanism, such as e-mail. The following example shows you the format of the XML string:

``` syntax
<PEERIDENTITYEXPORT VERSION="1.0">
   <PEERNAME>
     <!-- UTF-8 encoded peer name of the identity -->
   </PEERNAME>
   <DATA xmlns:dt="urn:schemas-microsoft-com:datatypes" dt:dt="bin.base64">
      <!-- base64 encoded / PFX encoded and encrypted IDC with the private key -->
   </DATA>
</PEERIDENTITYEXPORT>
```

The exported identity data can be retrieved by calling [**PeerIdentityImport**](/windows/win32/P2P/nf-p2p-peeridentityimport?branch=master), and passing in the XML string with the password supplied in the previous call to [**PeerIdentityExport**](/windows/win32/P2P/nf-p2p-peeridentityexport?branch=master). This function returns the peer name of the imported identity. The imported identity name and credentials can be used just like an identity name returned by [**PeerEnumIdentities**](/windows/win32/P2P/nf-p2p-peerenumidentities?branch=master) or [**PeerIdentityCreate**](/windows/win32/P2P/nf-p2p-peeridentitycreate?branch=master).

> [!Note]  
> When calling [**PeerIdentityExport**](/windows/win32/P2P/nf-p2p-peeridentityexport?branch=master), the application or API user must provide a strong password of sufficient length. This is important because the imported identity data contains the private key for the identity.

 

## Importing and Exporting a Group Identity Configuration

Peer Grouping allows a peer to export group configuration data from one endpoint to another by using specific import and export APIs. To import configuration data, the identity of the peer performing the import (and who previously performed the export) must be present on the computer where the configuration data is to be imported. This identity can be obtained by exporting and importing it by the methods specified in the previous section of this topic: [Importing and Exporting Peer Identity Data](#importing-and-exporting-peer-identity-data).

The group configuration data contains all of the information for an identity to join a group from a new endpoint. Specifically, the configuration data contains the GMC chain, group peer name, cloud name, scope, and a set of PNRP specific flags. For an identity that owns a group, a private key for the group is included in the group configuration information.

> [!Note]  
> When calling [**PeerGroupExportConfig**](/windows/win32/P2P/nf-p2p-peergroupexportconfig?branch=master), an application or API user must provide a strong password of sufficient length. This is important because the imported identity data contains the private key for the group.

 

To export the current peer group configuration, call [**PeerGroupExportConfig**](/windows/win32/P2P/nf-p2p-peergroupexportconfig?branch=master), passing in the handle to the group (obtained by a previous call to [**PeerGroupJoin**](/windows/win32/P2P/nf-p2p-peergroupjoin?branch=master), [**PeerGroupOpen**](/windows/win32/P2P/nf-p2p-peergroupopen?branch=master), or [**PeerGroupCreate**](/windows/win32/P2P/nf-p2p-peergroupcreate?branch=master)), and a password used to encrypt and protect the configuration file. This function returns an XML string that contains the configuration in the format of the following example, which can then be written to a file and passed to another computer by using an external transfer mechanism, such as email.

``` syntax
<PEERGROUPCONFIG VERSION="1.0">
  <IDENTITYPEERNAME>
    <!-- UTF-8 encoded peer name of the identity -->
  </IDENTITYPEERNAME>
  <GROUPPEERNAME>
    <!-- UTF-8 encoded peer name of the group -->
  </GROUPPEERNAME>
  <CLOUDNAME>
    <!-- UTF-8 encoded Unicode name of the cloud -->
  </CLOUDNAME>
  <SCOPE>
    <!-- UTF-8 encoded Unicode name of the scope: global, site-local, link-local -->
  </SCOPE>
  <CLOUDFLAGS>
    <!-- A DWORD that contains cloud-specific settings, represented as a string -->
  </CLOUDFLAGS>
  <GMC xmlns:dt="urn:schemas-microsoft-com:datatypes" dt:dt="bin.base64">
    <!-- base64/PKCS7 encoded GMC chain -->
  </GMC>
</PEERGROUPCONFIG>
```

After obtaining the group configuration as an XML string, the group can be imported by calling [**PeerGroupImportConfig**](/windows/win32/P2P/nf-p2p-peergroupimportconfig?branch=master) with the configuration XML string and the specific password supplied to [**PeerGroupExportConfig**](/windows/win32/P2P/nf-p2p-peergroupexportconfig?branch=master). This function returns an identity name and a group peer name, which can then be supplied to [**PeerGroupOpen**](/windows/win32/P2P/nf-p2p-peergroupopen?branch=master) and a connection to the group established.

 

 



