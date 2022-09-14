---
title: Name Formats for Unique SPNs
description: An SPN must be unique in the forest in which it is registered.
ms.assetid: dd3f9f7c-b64c-4bd8-924f-a8880ee3b71e
ms.tgt_platform: multiple
keywords:
- Name Formats for Unique SPNs AD
- Service Principal Name AD , Name Formats for
ms.topic: article
ms.date: 05/31/2018
---

# Name Formats for Unique SPNs

An SPN must be unique in the forest in which it is registered. If it is not unique, authentication will fail. The SPN syntax has four elements: two required elements and two additional elements that you can use, if necessary, to produce a unique name as listed in the following table.


```C++
<service class>/<host>:<port>/<service name>
```






| Element | Description | 
|---------|-------------|
| "&lt;service class&gt;" | A string that identifies the general class of service; for example, "SqlServer". There are well-known service class names, such as "www" for a web service or "ldap" for a directory service. In general, this can be any string that is unique to the service class. Be aware that the SPN syntax uses a forward slash (/) to separate elements, so this character cannot appear in a service class name. | 
| "&lt;host&gt;" | The name of the computer on which the service is running. This can be a fully qualified DNS name or a NetBIOS name. Be aware that NetBIOS names are not guaranteed to be unique in a forest, so an SPN that contains a NetBIOS name may not be unique. | 
| "&lt;port&gt;" | An optional port number to differentiate between multiple instances of the same service class on a single host computer. Omit this component if the service uses the default port for its service class. | 
| "&lt;service name&gt;" | An optional name used in the SPNs of a replicable service to identify the data or services provided by the service or the domain served by the service. This component can have one of the following formats:<ul><li>The distinguished name or objectGUID of an object in Active Directory Domain Services, such as a service connection point (SCP).</li><li>The DNS name of the domain for a service that provides a specified service for a domain as a whole.</li><li>The DNS name of an SRV or MX record.</li></ul> | 




 

The components present in a service's SPNs depend on how the service is identified and replicated. There are two basic scenarios: host-based services and replicable services.

## Host-based services

For a host-based service, the "&lt;service name&gt;" component is omitted because the service is uniquely identified by the service class and the name of the host computer on which the service is installed.


```C++
<service class>/<host>
```



The service class alone is sufficient to identify for clients the features that the service provides. You can install instances of the service class on many computers and each instance provides services that are identified with its host computer. FTP and Telnet are examples of host-based services. The SPNs of a host-based service instance can include the port number if the service uses a non-default port or there are multiple instances of the service on the host.


```C++
<service class>/<host>:<port>
```



## Replicable services

For a replicable service there can be one or many instances of the service (replicas), and clients do not differentiate which replica they connect to because each provides the same service. The SPNs for each replica have the same "&lt;service class&gt;" and "&lt;service name&gt;" components, where "&lt;service name&gt;" identifies more specifically the features provided by the service. Only the "&lt;host&gt;" and optional "&lt;port&gt;" components would vary from SPN to SPN.


```C++
<service class>/<host>:<port>/<service name>
```



An example of a replicable service would be an instance of a database service that provides access to a specified database. In this case, "&lt;service class&gt;" identifies the database application and "&lt;service name&gt;" identifies the specific database. "&lt;service name&gt;" could be the distinguished name of a service connection point (SCP) containing connection data for the database.


```C++
MyDBService/host1.example.com/CN=hrdb,OU=mktg,DC=example,DC=com
MyDBService/host2.example.com/CN=hrdb,OU=mktg,DC=example,DC=com
MyDBService/host3.example.com/CN=hrdb,OU=mktg,DC=example,DC=com
```



If clients will use the NetBIOS name to compose a service's SPN, each replica must also register an SPN containing the NetBIOS name.


```C++
MyDBService/host1/CN=hrdb,OU=mktg,DC=example,DC=com
MyDBService/host2/CN=hrdb,OU=mktg,DC=example,DC=com
MyDBService/host3/CN=hrdb,OU=mktg,DC=example,DC=com
```



Another example of a replicable service is one that provides services to an entire domain. In this case, the "&lt;service name&gt;" component is the DNS name of the domain being served. A Kerberos KDC is an example of this type of replicable service.

Be aware that if the DNS name of a computer changes, the system updates the "&lt;host&gt;" element for all registered SPNs for that host in the forest.

 

 




