---
title: Finding Server Host Systems
description: Finding server host systems by using string bindings and by querying a name service database for the location of a server program.
ms.assetid: 4aadda88-2109-481f-aa4b-b1983d81dec5
ms.topic: article
ms.date: 05/31/2018
---

# Finding Server Host Systems

A server host system is the computer that executes the distributed application's server program. There may be one or many server host systems on a network. How your client program finds a server to connect to depends on the needs of your program.

There are two methods of finding server host systems:

-   Using information stored in strings in the client source code, environment variables, or application-specific configuration files. Your client application can use the data in the string to compose a binding between the client and the server.
-   Querying a name service database for the location of a server program.

This section presents information on both of these techniques in the following topics:

-   [Using String Bindings](#using-string-bindings)
-   [Importing from Name Service Databases](#importing-from-name-service-databases)

## Using String Bindings

Applications can create bindings from information stored in strings. Your client application composes this information as a string, then calls the [**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding) function. The client must supply the following information to identify the server:

-   The interface name, the globally unique identifier (GUID) of the object, or UUID of the object. For more information, see [Generating Interface UUIDs](generating-interface-uuids.md) and [String UUID](string-uuid.md).
-   The transport type to communicate over, such as named pipes or TCP/IP. For details, see [Essential RPC Binding Terminology](essential-rpc-binding-terminology.md) and [Selecting a Protocol Sequence](selecting-a-protocol-sequence.md).
-   The network address or the name of the server host computer.
-   The endpoint of the server program on the server host computer. For more information, see [Finding Endpoints](finding-endpoints.md), and [Specifying Endpoints](specifying-endpoints.md).

(The object UUID and the endpoint information are optional.)

In the following examples, the *pszNetworkAddress* parameter and other parameters include embedded backslashes. The backslash is an escape character in the C programming language. Two backslashes are needed to represent each single literal backslash character. The string-binding structure must contain four backslash characters to represent the two literal backslash characters that precede the server name.

The following example shows that the server name must be preceded by eight backslashes so that four literal backslash characters will appear in the string-binding data structure after the **sprintf\_s** function processes the string.


```C++
/* client application */

char * pszUuid = "6B29FC40-CA47-1067-B31D-00DD010662DA";
char * pszProtocol = "ncacn_np";
char * pszNetworkAddress = "\\\\\\\\servername";
char * pszEndpoint = "\\\\pipe\\\\pipename";
char * pszString;
 
int len = 0;
 
len  = sprintf_s(pszString, strlen(pszUuid), "%s", pszUuid);
len += sprintf_s(pszString + len, strlen(pszProtocolSequence) + 2, "@%s:",
    pszProtocolSequence);
if (pszNetworkAddress != NULL)
    len += sprintf_s(pszString + len, strlen(pszNetworkAddress), "%s",
    pszNetworkAddress);
len += sprintf_s(pszString + len, strlen(pszEndpoint) + 2, "[%s]", pszEndpoint);
```



In the following example, the string binding appears as:

6B29FC40-CA47-1067-B31D-00DD010662DA@ncacn\_np:\\\\\\\\*servername*\[\\\\pipe\\\\*pipename*\]

The client then calls [**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding) to obtain the binding handle:


```C++
RPC_BINDING_HANDLE hBinding;
 
status = RpcBindingFromStringBinding(pszString, &hBinding);
//...
```



A convenience function, [**RpcStringBindingCompose**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcstringbindingcompose) assembles the object UUID, protocol sequence, network address, and endpoint in the correct syntax for the call to [**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding). You do not have to worry about putting the ampersand, colon, and the various components for each protocol sequence in the right place; you just supply the strings as parameters to the function. The run-time library even allocates the memory needed for the string binding.


```C++
char * pszNetworkAddress = "\\\\server";
char * pszEndpoint = "\\pipe\\pipename";
status = RpcStringBindingCompose(
            pszUuid,
            pszProtocolSequence,
            pszNetworkAddress,
            pszEndpoint,
            pszOptions,
            &pszString);
//...
status = RpcBindingFromStringBinding(
            pszString,
            &hBinding);
//...
```



Another convenience function, [**RpcBindingToStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingtostringbinding), takes a binding handle as input and produces the corresponding string binding.

## Importing from Name Service Databases

Name service databases store, among other things, binding handles and UUIDs. Your client application can search for either or both of these when it needs to bind to the server. For a discussion of the information that a name service stores, and the storage format, see [The RPC Name Service Database](the-rpc-name-service-database.md).

The RPC library provides two sets of functions that your client program can use to search the name service database. The names of one set begin with RpcNsBindingImport. The names of the other set begin with RpcNsBindingLookup. The difference between the two groups of functions is that the RpcNsBindingImport functions return a single binding handle per call and the RpcNsBindingLookup functions return groups of handles per call.

To begin a search with the RpcNsBindingImport functions, first call [**RpcNsBindingImportBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportbegina), as shown in the following code fragment.


```C++
RPC_STATUS status;
RPC_NS_HANDLE hNameServiceHandle;
 
status = RpcNsBindingImportBegin(
    RPC_C_NS_SYNTAX_DEFAULT,
    NULL,
    MyInterface_v1_0_c_ifspec,
    NULL,
    &hNameServiceHandle);
```



When the RPC functions search the name service database, they need a place to begin the search. In RPC terminology, this is called the entry name. Your client program passes the entry name as the second parameter to [**RpcNsBindingImportBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportbegina). This parameter can be **NULL** if you want to search the entire name service database. Alternatively, you can search the server entry by passing a server-entry name or search the group entry by passing a group-entry name. Passing an entry name restricts the search to the contents of that entry.

In the preceding example, the value RPC\_C\_NS\_SYNTAX\_DEFAULT is passed as the first parameter to [**RpcNsBindingImportBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportbegina). This selects the default entry name syntax. Currently, this is the only supported entry-name syntax.

Your client application can search the name service database for an interface name, a UUID, or both. If you want to have it search for an interface by name, pass the global interface variable that the MIDL compiler generates from your IDL file as the third parameter to [**RpcNsBindingImportBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportbegina). You'll find its declaration in the header file that the MIDL compiler generated when it generated the client stub. If you want your client program to search by UUID only, set the third parameter to **NULL**.

When searching the name service database for a UUID, set the fourth parameter of [**RpcNsBindingImportBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportbegina) to the UUID that you want to search for. If you are not searching for a UUID, set this parameter to **NULL**.

The [**RpcNsBindingImportBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportbegina) function passes the address of a name service–search context handle through its fifth parameter. You pass this parameter to other RpcNsBindingImport functions.

In particular, the next function your client application would call is [**RpcNsBindingImportNext**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportnext). Client programs use this function to retrieve compatible binding handles from the name service database. The following code fragment demonstrates how this function might be called:


```C++
RPC_STATUS status;
RPC_BINDING_HANDLE hBindingHandle;
// The variable hNameServiceHandle is a valid name service search 
// context handle obtained from the RpcNsBindingBegin function.
 
status = RpcNsBindingImportNext(hNameServiceHandle, &hBindingHandle);
```



Once it has called the [**RpcNsBindingImportNext**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportnext) function to obtain a binding handle, your client application can determine if the handle it received is acceptable. If not, your client program can execute a loop and call **RpcNsBindingImportNext** again to see if the name service contains a more appropriate handle. For each call to **RpcNsBindingImportNext**, there must be a corresponding call to RpcNsBindingFree. When your search is complete, call the [**RpcNsBindingImportDone**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportdone) function to free the lookup context.

After your client application has an acceptable binding handle, it should check to ensure that the server application is running. There are two methods your client can use to perform this verification. The first is to call a function in the client interface. If the server program is running, the call will complete. If not, the call will fail. A better way to verify that the server is running is to invoke [**RpcEpResolveBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepresolvebinding), followed by a call to [**RpcMgmtIsServerListening**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtisserverlistening). For more information on the name service database, see [The RPC Name Service Database](the-rpc-name-service-database.md).

 

 




