---
description: This configuration creates an IPsec Security Association (SA) between two hosts on the same subnet to perform authentication using the Authentication Header (AH) and the Message Digest 5 (MD5) hashing algorithm.
ms.assetid: ed88d8ee-ac65-4310-a988-ead50ff743fd
title: 'Configuration 3: Using IPsec Between Two Local-link Hosts'
ms.topic: article
ms.date: 05/31/2018
---

# Configuration 3: Using IPsec Between Two Local-link Hosts

This configuration creates an IPsec Security Association (SA) between two hosts on the same subnet to perform authentication using the Authentication Header (AH) and the Message Digest 5 (MD5) hashing algorithm. In this example, the configuration shown secures all traffic between two neighboring hosts: Host 1, with the link-local address FE80::2AA:FF:FE53:A92C, and Host 2, with the link-local address FE80::2AA:FF:FE92:D0F1.

**To use IPsec between two local-link hosts**

1.  On Host 1, create blank security association (SAD) and security policy (SPD) files by using the ipsec6 c command. In this example, the Ipsec6.exe command is ipsec6 c test. This creates two files to manually configure security associations (Test.sad) and security policies (Test.spd).
2.  On Host 1, edit the SPD file to add a security policy that secures all traffic between Host 1 and Host 2.

    The following table shows the security policy added to the Test.spd file before the first entry for this example (the first entry in the Test.spd file was not modified).

    | SPD file field name | Example value              |
    |---------------------|----------------------------|
    | **Policy**          | 2                          |
    | **RemoteIPAddr**    | **FE80::2AA:FF:FE92:D0F1** |
    | **LocalIPAddr**     | \*                         |
    | **RemotePort**      | \*                         |
    | **Protocol**        | \*                         |
    | **LocalPort**       | \*                         |
    | **IPSecProtocol**   | **AH**                     |
    | **IPSecMode**       | **TRANSPORT**              |
    | **RemoteGWIPAddr**  | \*                         |
    | **SABundleIndex**   | **NONE**                   |
    | **Direction**       | **BIDIRECT**               |
    | **Action**          | **APPLY**                  |
    | **InterfaceIndex**  | 0                          |

    

     

    Place a semicolon at the end of the line configuring this security policy. The policy entries must be placed in decreasing numerical order.

3.  On Host 1, edit the SAD file, adding SA entries to secure all traffic between Host 1 and Host 2. Two security associations must be created, one for traffic to Host 2 and one for traffic from Host 2.

    The following table shows the first SA entry added to the Test.sad file for this example (for traffic to Host 2).

    | SAD file field name | Example value              |
    |---------------------|----------------------------|
    | **SAEntry**         | 2                          |
    | **SPI**             | 3001                       |
    | **SADestIPAddr**    | **FE80::2AA:FF:FE92:D0F1** |
    | **DestIPAddr**      | **POLICY**                 |
    | **SrcIPAddr**       | **POLICY**                 |
    | **Protocol**        | **POLICY**                 |
    | **DestPort**        | **POLICY**                 |
    | **SrcPort**         | **POLICY**                 |
    | **AuthAlg**         | **HMAC-MD5**               |
    | **KeyFile**         | **Test.key**               |
    | **Direction**       | **OUTBOUND**               |
    | **SecPolicyIndex**  | 2                          |

    

     

    Place a semicolon at the end of the line configuring this SA.

    The following table shows the second SA entry added to the Test.sad file for this example (for traffic from Host 2).

    | SAD file field name | Example value              |
    |---------------------|----------------------------|
    | **SAEntry**         | 1                          |
    | **SPI**             | 3000                       |
    | **SADestIPAddr**    | **FE80::2AA:FF:FE53:A92C** |
    | **DestIPAddr**      | **POLICY**                 |
    | **SrcIPAddr**       | **POLICY**                 |
    | **Protocol**        | **POLICY**                 |
    | **DestPort**        | **POLICY**                 |
    | **SrcPort**         | **POLICY**                 |
    | **AuthAlg**         | **HMAC-MD5**               |
    | **KeyFile**         | **Test.key**               |
    | **Direction**       | **INBOUND**                |
    | **SecPolicyIndex**  | 2                          |

    

     

    Place a semicolon at the end of the line configuring this SA. The SA entries must be placed in decreasing numerical order.

4.  On Host 1, create a text file that contains a text string used to authenticate the SAs created with Host 2. In this example, the file Test.key is created with the contents "This is a test". You must include double quotes around the key string in order for the key to be read by the ipsec6 tool.

    The Microsoft IPv6 Technology Preview only supports manually configured keys for the authentication of IPsec SAs. The manual keys are configured by creating text files that contain the text string of the manual key. In this example, the same key for the SAs is used in both directions. You can use different keys for inbound and outbound SAs by creating different key files and referencing them with the KeyFile field in the SAD file.

5.  On Host 2, create blank security association (SAD) and security policy (SPD) files by using the ipsec6 c command. In this example, the Ipsec6.exe command is ipsec6 c test. This creates two files with blank entries for manually configuring security associations (Test.sad) and security policies (Test.spd).

    To simplify the example, the same file names for the SAD and SPD files are used on Host 2. You can choose to use different file names on each host.

6.  On Host 2, edit the SPD file to add a security policy that secures all traffic between Host 2 and Host 1.

    The following table shows the security policy entry added before the first entry to the Test.spd file for this example (the first entry in the Test.spd file was not modified).

    | SPD file field name | Example value              |
    |---------------------|----------------------------|
    | **Policy**          | 2                          |
    | **RemoteIPAddr**    | **FE80::2AA:FF:FE53:A92C** |
    | **LocalIPAddr**     | \*                         |
    | **RemotePort**      | \*                         |
    | **Protocol**        | \*                         |
    | **LocalPort**       | \*                         |
    | **IPSecProtocol**   | **AH**                     |
    | **IPSecMode**       | **TRANSPORT**              |
    | **RemoteGWIPAddr**  | \*                         |
    | **SABundleIndex**   | **NONE**                   |
    | **Direction**       | **BIDIRECT**               |
    | **Action**          | **APPLY**                  |
    | **InterfaceIndex**  | 0                          |

    

     

    Place a semicolon at the end of the line configuring this security policy. The policy entries must be placed in decreasing numerical order.

7.  On Host 2, edit the SAD file, adding SA entries to secure all traffic between Host 2 and Host 1. Two security associations must be created-one for traffic to Host 1 and one for traffic from Host 1.

    The following table shows the first SA added to the Test.sad file for this example (for traffic from Host 1).

    | SAD file field name | Example value              |
    |---------------------|----------------------------|
    | **SAEntry**         | 2                          |
    | **SPI**             | 3001                       |
    | **SADestIPAddr**    | **FE80::2AA:FF:FE92:D0F1** |
    | **DestIPAddr**      | **POLICY**                 |
    | **SrcIPAddr**       | **POLICY**                 |
    | **Protocol**        | **POLICY**                 |
    | **DestPort**        | **POLICY**                 |
    | **SrcPort**         | **POLICY**                 |
    | **AuthAlg**         | **HMAC-MD5**               |
    | **KeyFile**         | **Test.key**               |
    | **Direction**       | **INBOUND**                |
    | **SecPolicyIndex**  | 2                          |

    

     

    Place a semicolon at the end of the line configuring this SA.

    The following table shows the second SA entry added to the Test.sad file for this example (for traffic to Host 1).

    | SAD file field name | Example value              |
    |---------------------|----------------------------|
    | **SAEntry**         | 1                          |
    | **SPI**             | 3000                       |
    | **SADestIPAddr**    | **FE80::2AA:FF:FE53:A92C** |
    | **DestIPAddr**      | **POLICY**                 |
    | **SrcIPAddr**       | **POLICY**                 |
    | **Protocol**        | **POLICY**                 |
    | **DestPort**        | **POLICY**                 |
    | **SrcPort**         | **POLICY**                 |
    | **AuthAlg**         | **HMAC-MD5**               |
    | **KeyFile**         | **Test.key**               |
    | **Direction**       | **OUTBOUND**               |
    | **SecPolicyIndex**  | 2                          |

    

     

    Place a semicolon at the end of the line configuring this SA. The SA entries must be placed in decreasing numerical order.

8.  On Host 2, create a text file that contains a text string used to authenticate the SAs created with Host 1. In this example, the file Test.key is created with the contents "This is a test". You must include double quotes around the key string in order for the key to be read by the ipsec6 tool.
9.  On Host 1, add the configured security policies and SAs from the SPD and SAD files using the ipsec6 a command. In this example, the ipsec6 a test command is run on Host 1.
10. On Host 2, add the configured security policies and SAs from the SPD and SAD files by using the ipsec6 a command. In this example, the ipsec6 a test command is run on Host 2.
11. Ping Host 1 from Host 2 with the ping6 command.

    If you capture the traffic using Microsoft Network Monitor or another packet sniffer, you should see the exchange of ICMPv6 Echo Request and Echo Reply messages with an Authentication Header between the IPv6 header and the ICMPv6 header.

## Related topics

<dl> <dt>

[Recommended Configurations for IPv6](recommended-configurations-2.md)
</dt> <dt>

[Single subnet with link-local addresses](configuration-1-single-subnet-with-link-local-addresses-2.md)
</dt> <dt>

[IPv6 traffic between nodes on different subnets of an IPv4 internetwork (6to4)](configuration-2-ipv6-traffic-between-nodes-on-different-subnets-of-an-ipv4-internetwork-6to4--2.md)
</dt> </dl>

 

 



