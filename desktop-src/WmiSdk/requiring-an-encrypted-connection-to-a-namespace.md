---
description: You can require that client scripts and applications establish an encrypted connection for authentication by adding the RequiresEncryption qualifier to the Managed Object Format (MOF) .mof file that creates the namespace.
ms.assetid: 07b225a2-3834-4879-beae-f5b9180d112f
ms.tgt_platform: multiple
title: Requiring an Encrypted Connection to a Namespace
ms.topic: article
ms.date: 05/31/2018
---

# Requiring an Encrypted Connection to a Namespace

You can require that client scripts and applications establish an encrypted connection for authentication by adding the **RequiresEncryption** qualifier to the Managed Object Format (MOF) .mof file that creates the namespace.


An encrypted connection to a WMI namespace specifies **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY** (or **PktPrivacy** in a script) for authentication. The **RequiresEncryption** qualifier causes WMI to reject any incoming data requests unless they explicitly use encrypted authentication. For more information, see [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md) or [Setting Authentication Using C++](setting-authentication-using-c-.md).

You can also modify an existing namespace by adding this attribute and then compile the MOF file again. **RequiresEncryption** is used in [*MOF*](gloss-m.md) with the [pragma namespace](pragma-namespace.md) preprocessor instruction.

The following procedure sets the namespace to require an encrypted connection.

**To set required encryption**

1.  Create a Managed Object Format (MOF) file or modify your existing MOF file that defines the namespace.

    The following code example shows the namespace that will be modified is *root\\MyNamespace* and the file is named *MyNamespace\_security.mof*. **RequiresEncryption** has a Boolean datatype so it must be set to **True** or **False**.

    ```mof
    #pragma namespace("\\\\.\\Root\\MyNamespace") 

    [RequiresEncryption(TRUE)] 
    instance of __systemSecurity { };
    ```

    

2.  Run [**mofcomp.exe**](mofcomp.md) to compile the MOF file.

    **c:\\mofcomp MyNamespace\_security.mof**

    In C++, use the [**IMoFCompiler**](/windows/desktop/api/Wbemcli/nn-wbemcli-imofcompiler) methods.

WMI rejects a client that uses the default authentication level because DCOM negotiates the security to the level required by the SVCHOST process in which the WMI service is running. For more information about service hosts, see [Provider Hosting and Security](provider-hosting-and-security.md). For more information about setting authentication levels when connecting to WMI namespaces, see [Setting the Default Process Security Level Using C++](setting-the-default-process-security-level-using-c-.md), [Setting Authentication Using C++](setting-authentication-using-c-.md), or [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

When returning data on an asynchronous callback connection, WMI returns an access denied message to the requesting computer. WMI also makes a log entry in the NT Event Log of the computer with the encrypted namespace stating that a secure connection cannot be established to the client.

Starting with Windows Vista, the WbemCore.log file no longer exists. You can check the NT Event Log for entries indicating rejected inbound data requests to namespaces that require encryption.

## Related topics

<dl> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dt>

[**WbemAuthenticationLevelEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemauthenticationlevelenum)
</dt> <dt>

[Securing a Remote WMI Connection](securing-a-remote-wmi-connection.md)
</dt> </dl>

 

 



