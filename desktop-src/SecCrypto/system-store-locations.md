---
description: A system store is a collection that consists of one or more physical sibling stores.
ms.assetid: 41fe9366-4c17-43bb-91d6-934c7aa87a2d
title: System Store Locations
ms.topic: article
ms.date: 05/31/2018
---

# System Store Locations

A system store is a collection that consists of one or more physical sibling stores. For each system store, there are predefined physical sibling stores. After opening a system store such as MY at CERT\_SYSTEM\_STORE\_CURRENT\_USER, the store provider calls [**CertOpenStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopenstore) to open each of the physical stores in the system store collection. In the open process, each of these physical stores is added to the system store collection using [**CertAddStoreToCollection**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddstoretocollection). All certificates in those physical stores are available through the logical system store collection.

For each system store location, the predefined systems stores are:

-   MY
-   Root
-   Trust
-   CA

In CERT\_SYSTEM\_STORE\_CURRENT\_USER, there is also a predefined UserDS store. A smart card store is planned for this location.

Here are the system stores followed by further remarks:

-   [CERT\_SYSTEM\_STORE\_CURRENT\_USER](#cert_system_store_current_user)
-   [CERT\_SYSTEM\_STORE\_LOCAL\_MACHINE](#cert_system_store_local_machine)
-   [CERT\_SYSTEM\_STORE\_CURRENT\_SERVICE](#cert_system_store_current_service)
-   [CERT\_SYSTEM\_STORE\_SERVICES](#cert_system_store_services)
-   [CERT\_SYSTEM\_STORE\_USERS](#cert_system_store_users)
-   [CERT\_SYSTEM\_CURRENT\_USER\_GROUP\_POLICY](#cert_system_current_user_group_policy)
-   [CERT\_SYSTEM\_LOCAL\_MACHINE\_GROUP\_POLICY](#cert_system_local_machine_group_policy)
-   [CERT\_SYSTEM\_STORE\_LOCAL\_MACHINE\_ENTERPRISE](#cert_system_store_local_machine_enterprise)
-   [Remarks](#remarks)

### CERT\_SYSTEM\_STORE\_CURRENT\_USER

CERT\_SYSTEM\_STORE\_CURRENT\_USER system stores are at the following registry location:

```
HKEY_CURRENT_USER
   Software
      Microsoft
         SystemCertificates
```

The predefined physical stores associated with those system stores are as follows.



| System store | Physical store                                           |
|--------------|----------------------------------------------------------|
| MY           | .Default                                                 |
| Root         | .Default.LocalMachine<br/> .SmartCard<br/>   |
| Trust        | .Default.GroupPolicy<br/> .LocalMachine<br/> |
| CA           | .Default.GroupPolicy<br/> .LocalMachine<br/> |
| UserDS       | .UserCertificate                                         |



 

### CERT\_SYSTEM\_STORE\_LOCAL\_MACHINE

CERT\_SYSTEM\_STORE\_LOCAL\_MACHINE system stores are at the following registry location:

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         SystemCertificates
```

The predefined physical stores are associated with those system stores are as follows.



| System store | Physical store                                                                                    |
|--------------|---------------------------------------------------------------------------------------------------|
| MY           | .Default                                                                                          |
| Root         | .Default.AuthRoot<br/> .GroupPolicy<br/> .Enterprise<br/> .SmartCard<br/> |
| Trust        | .Default.GroupPolicy<br/> .Enterprise<br/>                                            |
| CA           | .Default.GroupPolicy<br/> .Enterprise <br/>                                           |



 

### CERT\_SYSTEM\_STORE\_CURRENT\_SERVICE

CERT\_SYSTEM\_STORE\_CURRENT\_SERVICE system stores are at the following registry location:

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Cryptography
            Services
               ServiceName
                  SystemCertificates
```

The predefined physical stores associated with those system stores are as follows.



| System store | Physical store                   |
|--------------|----------------------------------|
| MY           | .Default                         |
| Root         | .Default.LocalMachine<br/> |
| Trust        | .Default.LocalMachine<br/> |
| CA           | .Default.LocalMachine<br/> |



 

### CERT\_SYSTEM\_STORE\_SERVICES

CERT\_SYSTEM\_STORE\_SERVICES system stores are at the following registry location:

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Cryptography
            Services
               ServiceName
                  SystemCertificates
```

The predefined physical stores associated with those system stores are as follows.



| System store       | Physical store                   |
|--------------------|----------------------------------|
| ServiceName\\MY    | .Default                         |
| ServiceName\\Root  | .Default.LocalMachine<br/> |
| ServiceName\\Trust | .Default.LocalMachine<br/> |
| ServiceName\\CA    | .Default.LocalMachine<br/> |



 

### CERT\_SYSTEM\_STORE\_USERS

CERT\_SYSTEM\_STORE\_USERS system stores are at the following registry location:

```
HKEY_USERS
   UserName
      Software
         Microsoft
            SystemCertificates
```

The predefined physical stores associated with those system stores are as follows.



| System store  | Physical store                   |
|---------------|----------------------------------|
| userid\\MY    | .Default.LocalMachine<br/> |
| userid\\Root  | .Default.LocalMachine<br/> |
| userid\\Trust | .Default.LocalMachine<br/> |
| userid\\CA    | .Default.LocalMachine<br/> |



 

### CERT\_SYSTEM\_CURRENT\_USER\_GROUP\_POLICY

CERT\_SYSTEM\_CURRENT\_USER\_GROUP\_POLICY system stores are at the following registry location:

```
HKEY_CURRENT_USER
   Software
      Policy
         Microsoft
            SystemCertificates
```

### CERT\_SYSTEM\_LOCAL\_MACHINE\_GROUP\_POLICY

CERT\_SYSTEM\_LOCAL\_MACHINE\_GROUP\_POLICY system stores are at the following registry location:

```
HKEY_LOCAL_MACHINE
   Software
      Policy
         Microsoft
            SystemCertificates
```

### CERT\_SYSTEM\_STORE\_LOCAL\_MACHINE\_ENTERPRISE

CERT\_SYSTEM\_STORE\_LOCAL\_MACHINE\_ENTERPRISE contains certificates shared across domains in the enterprise and downloaded from the global enterprise directory. To synchronize the client's enterprise store, the enterprise directory is polled every eight hours and certificates are downloaded automatically in the background.

The predefined physical stores associated with these system stores are as follows.



| System store | Physical store |
|--------------|----------------|
| MY           | .Default       |
| Root         | .Default       |
| Trust        | .Default       |
| CA           | .Default       |



 

### Remarks

Additional physical stores can be associated with a system store by using [**CertRegisterPhysicalStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certregisterphysicalstore).

CERT\_SYSTEM\_STORE\_SERVICE and CERT\_SYSTEM\_STORE\_USERS stores are opened by prefixing the name of the store in the string passed to *pvPara* with the service or user name such as *ServiceName*\\**Trust** or **.Default**\\**MY**. The CERT\_SYSTEM\_STORE\_SERVICES or CERT\_SYSTEM\_STORE\_USERS location can open the same store in CERT\_SYSTEM\_CURRENT\_SERVICE or CERT\_SYSTEM\_STORE\_CURRENT\_USER by using the textual [*security identifier*](../secgloss/s-gly.md) (SID) of the current service or user.

Stores in CERT\_SYSTEM\_STORE\_USER\_GROUP\_POLICY and CERT\_SYSTEM\_LOCAL\_MACHINE\_GROUP\_POLICY in a network setting are downloaded to the client computer from the Group Policy Template (GPT) during computer startup or user logon. These stores can be updated on the client computer after startup or logon when the GPT is changed on the domain server by an administrator. The [**CertControlStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcontrolstore) function allows an application to be notified when stores in either of these locations have changed.

The following system store locations can be opened remotely:

-   CERT\_SYSTEM\_STORE\_LOCAL\_MACHINE
-   CERT\_SYSTEM\_STORE\_LOCAL\_MACHINE\_GROUP\_POLICY
-   CERT\_SYSTEM\_STORE\_SERVICES
-   CERT\_SYSTEM\_STORE\_USERS

System store locations are opened remotely by prefixing the store name in the string passed to *pvPara* with the computer name. Examples of remote system store names are:

-   *ComputerName*\\**CA**
-   \\\\*ComputerName*\\**CA**
-   *ComputerName*\\*ServiceName*\\**Trust**
-   \\\\*ComputerName*\\*ServiceName*\\**Trust**

 

 
