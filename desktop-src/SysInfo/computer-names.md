---
Description: 'DNS names consist of one or more components separated by a period (for example, msdn.microsoft.com).'
ms.assetid: '7e083cb5-cf0a-4284-8b54-dac856910c44'
title: Computer Names
---

# Computer Names

DNS names consist of one or more components separated by a period (for example, msdn.microsoft.com). Each component can be up to 63 bytes. Each name can be up to 255 bytes total. DNS names are represented in the UTF-8 character set or Unicode. The name is not case sensitive. For more information, see [**DnsValidateName**](https://msdn.microsoft.com/library/windows/desktop/ms682032).

A computer is uniquely identified by its fully qualified DNS name, which consists of its DNS host name and the name of the DNS domain to which it is assigned. To retrieve a computer's fully qualified DNS name, DNS host name, or DNS domain name, call the [**GetComputerNameEx**](getcomputernameex.md) function. To set a computer's DNS host name or DNS domain name, call the [**SetComputerNameEx**](setcomputernameex.md) function. Name changes do not take effect until the user restarts the computer.

NetBIOS names consist of up to 15 bytes of OEM characters including letters, digits, hyphens, and periods. Some characters are specific to the character set. NetBIOS names are typically represented in the OEM character set. The OEM character set depends on the locale. Some OEM character sets represent certain characters as two bytes. NetBIOS names, by convention, are represented in uppercase where the translation algorithm from lowercase to uppercase is OEM character set dependent.

The [**SetComputerNameEx**](setcomputernameex.md) and [**GetComputerNameEx**](getcomputernameex.md) functions can also set and retrieve the computer's NetBIOS name. By convention, the NetBIOS name and the DNS host name are interdependent. When you modify the DNS name, the NetBIOS name is also updated. The NetBIOS name is the OEM representation of the DNS host name up to MAX\_COMPUTERNAME\_LENGTH characters. If you set a DNS host name of more than MAX\_COMPUTERNAME\_LENGTH characters, the NetBIOS name is set to a truncated version of the DNS host name. Otherwise, the whole DNS host name is translated into the OEM NetBIOS name. Warning: If you modify the NetBIOS name so that it is not a truncated mapping of the DNS name, you will break applications that use functions such as [**DnsHostnameToComputerName**](dnshostnametocomputername.md) which rely on this convention.

 

 



