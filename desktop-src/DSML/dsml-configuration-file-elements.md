---
title: DSML Configuration File Elements
description: The following describes the elements found in the DSML configuration file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '5f6e7cff-556d-42ec-8042-479aeadaa096'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# DSML Configuration File Elements

The following describes the elements found in the DSML configuration file.

All the element tags inside the **virtualDirectory** element are optional. To omit an element tag, omit the entire line, including the surrounding XML elements. For example, to omit **serverName**, omit **&lt;server&gt;serverName&lt;/server&gt;**.

The elements contained in the **virtualDirectory** element of the DSML configuration file are listed in the following list.

<dl> <dt>

<span id="serverName"></span><span id="servername"></span><span id="SERVERNAME"></span>**serverName**
</dt> <dd>

Specifies the DNS name of the Active Directory server or domain against which to perform LDAP operations. If **serverName** is omitted, DSML Services for Windows connects to a domain controller for the domain to which the web server computer account belongs. If a domain name is specified, it connects to a DC for that domain. If a server name is specified, it connects to that specific server.

</dd> <dt>

<span id="portNumber"></span><span id="portnumber"></span><span id="PORTNUMBER"></span>**portNumber**
</dt> <dd>

Specifies the port number on the Active Directory server to which to connect. The default is port 389.

</dd> <dt>

<span id="enableSSL"></span><span id="enablessl"></span><span id="ENABLESSL"></span>**enableSSL**
</dt> <dd>

Specifies whether SSL encryption will be used when connecting to the Active Directory server. The default value is **false**.

</dd> <dt>

<span id="enableLDAPSigning"></span><span id="enableldapsigning"></span><span id="ENABLELDAPSIGNING"></span>**enableLDAPSigning**
</dt> <dd>

Specifies whether the LDAP connection between a server running DSML Services for Windows and the Active Directory server will use certificate signing. This option does not affect the connection between the client application and a server running DSML Services for Windows. The default value is **false**, meaning digital signing is not used.

</dd> <dt>

<span id="enableLDAPSealing"></span><span id="enableldapsealing"></span><span id="ENABLELDAPSEALING"></span>**enableLDAPSealing**
</dt> <dd>

Specifies whether the LDAP connection between a server running DSML Services for Windows and the Active Directory server will use data encryption. This option does not affect the connection between the client application and a server running DSML Services for Windows. The default value is **false**, meaning encryption not used.

</dd> <dt>

<span id="enableReadOnlyMode"></span><span id="enablereadonlymode"></span><span id="ENABLEREADONLYMODE"></span>**enableReadOnlyMode**
</dt> <dd>

Specifies whether read-only mode is enabled. If enabled, a server running DSML Services for Windows will only process **searchRequest** and **compareRequest** operations. Other requests, for example, requests to add to, delete from, or modify the directory, will fail. The default value is **false**.

</dd> <dt>

<span id="connTime"></span><span id="conntime"></span><span id="CONNTIME"></span>**connTime**
</dt> <dd>

Specifies the time, in seconds, to wait when trying to establish a LDAP connection to the Active Directory server. The default setting is no timeout period. It is recommended that you specify a timeout period.

</dd> <dt>

<span id="operTime"></span><span id="opertime"></span><span id="OPERTIME"></span>**operTime**
</dt> <dd>

Specifies the time, in seconds, to wait for an individual LDAP operation to complete. The default is no timeout period. It is recommended that you specify a timeout period.

</dd> <dt>

<span id="numberOfConnections"></span><span id="numberofconnections"></span><span id="NUMBEROFCONNECTIONS"></span>**numberOfConnections**
</dt> <dd>

Specifies the maximum number of simultaneous LDAP connections to keep open to the Active Directory server. The default number is five. The higher this number, the greater the number of incoming DSML requests that can be simultaneously processed.

</dd> <dt>

<span id="maxReqsPerBatch"></span><span id="maxreqsperbatch"></span><span id="MAXREQSPERBATCH"></span>**maxReqsPerBatch**
</dt> <dd>

Specifies the maximum number of operations that a server running DSML Services for Windows will accept in a single DSML **batchRequest**. Requests which contain more than that number of operations will not be processed, and an error will be returned. The default value is 1000. For optimal performance, it is recommended not to set this option to a value greater than 4000.

</dd> <dt>

<span id="chaseReferralsType"></span><span id="chasereferralstype"></span><span id="CHASEREFERRALSTYPE"></span>**chaseReferralsType**
</dt> <dd>

Specifies the type of referral chasing used by the Active Directory server when a referral is generated. The allowable values are **never**, **always**, **subordinate**, and **external**. The default value is **never**, meaning referral chasing is not used.

</dd> <dt>

<span id="totalSessions"></span><span id="totalsessions"></span><span id="TOTALSESSIONS"></span>**totalSessions**
</dt> <dd>

Specifies the total number of outstanding active sessions allowed. If the total number reaches the maximum, and a client requests a new session, the server will reject all subsequent new session requests until the number of outstanding active sessions is less than the maximum number specified. The default value is 100 sessions.

</dd> <dt>

<span id="sessionsPerIP"></span><span id="sessionsperip"></span><span id="SESSIONSPERIP"></span>**sessionsPerIP**
</dt> <dd>

Specifies the number of sessions allowed for a given IP address. The default value is five sessions.

</dd> <dt>

<span id="useIPMatching"></span><span id="useipmatching"></span><span id="USEIPMATCHING"></span>**useIPMatching**
</dt> <dd>

Specifies whether the server should verify that the IP address matches that of the original creator of the session when the client requests a session ID. The default value is **true**.

</dd> <dt>

<span id="useCredentialMatching"></span><span id="usecredentialmatching"></span><span id="USECREDENTIALMATCHING"></span>**useCredentialMatching**
</dt> <dd>

Specifies whether the server should verify that the user credentials match those of the original creator of the session when the client requests a session ID. The default value is **true**.

</dd> <dt>

<span id="timeToLive"></span><span id="timetolive"></span><span id="TIMETOLIVE"></span>**timeToLive**
</dt> <dd>

Specifies the time, in seconds, that the session should live before it is declared to be expired. Each client request with the session ID revitalizes the TTL. If there is no activity beyond the TTL, the session will end. The default value is 600 seconds.

</dd> </dl>

## Related topics

<dl> <dt>

[Manually Configuring DSML Services for Windows](manually-configuring-dsml-services-for-windows.md)
</dt> </dl>

 

 




