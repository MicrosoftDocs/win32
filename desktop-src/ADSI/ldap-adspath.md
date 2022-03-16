---
title: LDAP ADsPath
description: This topic shows the syntax that you should use for the LDAP ADsPath.
ms.assetid: adacf6af-8683-4c3c-91bf-9489f2d5d817
ms.tgt_platform: multiple
keywords:
- LDAP ADsPath
- ADsPath, LDAP, description
ms.topic: article
ms.date: 05/31/2018
---

# LDAP ADsPath

The Microsoft LDAP provider ADsPath requires the following format.


```C++
LDAP://HostName[:PortNumber][/DistinguishedName]
```



> [!Note]  
> The left and right bracket characters (\[ \]) indicate optional parameters; it is not a literal part of the binding string.

 

The "HostName" can be a computer name, an IP address, or a domain name. A server name can also be specified in the binding string. Most LDAP providers follow a model that requires a server name to be specified.

The "PortNumber" specifies the port to be used for the connection. If no port number is specified, the LDAP provider uses the default port number. The default port number is 389 if not using an SSL connection or 636 if using an SSL connection.

The "DistinguishedName" specifies the distinguished name of a specific object. A distinguished name for a given object is guaranteed to be unique.

The following table lists examples of binding strings.



| LDAP ADsPath example                                      | Description                                                |
|-----------------------------------------------------------|------------------------------------------------------------|
| LDAP:                                                     | Bind to the root of the LDAP namespace.                    |
| LDAP://server01                                           | Bind to a specific server.                                 |
| LDAP://server01:390                                       | Bind to a specific server using the specified port number. |
| LDAP://CN=Jeff Smith,CN=users,DC=fabrikam,DC=com          | Bind to a specific object.                                 |
| LDAP://server01/CN=Jeff Smith,CN=users,DC=fabrikam,DC=com | Bind to a specific object through a specific server.       |



 

If Kerberos authentication is required for the successful completion of a specific directory request, the binding string must use either a serverless ADsPath, such as LDAP://CN=Jeff Smith,CN=users,DC=fabrikam,DC=com, or it must use an ADsPath with a fully qualified DNS server name, such as LDAP://server01.fabrikam.com/CN=Jeff Smith,CN=users,DC=fabrikam,DC=com. Binding to the server using a flat NETBIOS name or a short DNS name, for example, using the name server01 instead of server01.fabrikam.com, is not guaranteed to yield Kerberos authentication.

For more information and examples of LDAP binding strings, as well as a description of special characters that can be used in LDAP binding strings, see LDAP ADsPath.

**Windows 2000 with SP1 and later:** With the LDAP provider, if a binding string includes a server name, you can increase performance by using the **ADS\_SERVER\_BIND** flag with the [**ADsOpenObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsopenobject) function or the [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/Iads/nf-iads-iadsopendsobject-opendsobject) method. The **ADS\_SERVER\_BIND** flag indicates that a server name was specified, which enables ADSI to avoid additional, unnecessary network traffic.

## LDAP Special Characters

LDAP has several special characters which are reserved for use by the LDAP API. The list of special characters can be found in [Distinguished Names](/previous-versions/windows/desktop/ldap/distinguished-names). To use one of these characters in an ADsPath without generating an error, the character must be preceded by a backslash (\\) character. This is known as *escaping* the character. For example, if a user name is given in the form of "\<last name\>,\<first name\>", the comma in the name value must be escaped. The resulting string would look like this:


```C++
LDAP://CN=Smith\,Jeff,CN=users,DC=fabrikam,DC=com
```



The escaped character can also be specified by its two digit hexadecimal character code. This is shown in the following example.


```C++
LDAP://CN=Smith\2CJeff,CN=users,DC=fabrikam,DC=com
```



Non-printable characters, such as the line feed and carriage return, must be escaped and specified by their two digit hexadecimal character code. This is shown in the following example.


```C++
LDAP://CN=Line\0AFeed,CN=users,DC=fabrikam,DC=com
```



## For More Information

For more information about the distinguished name notation used by LDAP-compliant directory services, see [https://www.ietf.org/rfc/rfc1779.txt](https://www.ietf.org/rfc/rfc1779.txt).

 

 