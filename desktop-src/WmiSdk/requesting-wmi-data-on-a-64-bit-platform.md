---
description: By default, an application or script receives data from the corresponding provider when two versions of providers exist.
ms.assetid: 379d934e-e010-4a03-8dc1-121be43e4c6f
ms.tgt_platform: multiple
title: Requesting WMI Data on a 64-bit Platform
ms.topic: article
ms.date: 05/31/2018
---

# Requesting WMI Data on a 64-bit Platform

By default, an application or script receives data from the corresponding provider when two versions of providers exist. The 32-bit provider returns data to a 32-bit application, including all scripts, and the 64-bit provider returns data to the 64-bit compiled applications. However, an application or script can request data from the nondefault provider, if it exists, by notifying WMI through flags on method calls.

## Context Flags

The **\_\_ProviderArchitecture** and **\_\_RequiredArchitecture** string flags have a set of values handled by WMI but not defined in SDK header or type library files. The values are placed in a context parameter to signal WMI that it should request data from the nondefault provider.

The following lists the flags and their possible values.

<dl> <dt>

<span id="__ProviderArchitecture"></span><span id="__providerarchitecture"></span><span id="__PROVIDERARCHITECTURE"></span>**\_\_ProviderArchitecture**
</dt> <dd>

Integer value, either 32 or 64, that specifies the 32-bit or 64-bit version.

</dd> <dt>

<span id="__RequiredArchitecture"></span><span id="__requiredarchitecture"></span><span id="__REQUIREDARCHITECTURE"></span>**\_\_RequiredArchitecture**
</dt> <dd>

Boolean value used in addition to **\_\_ProviderArchitecture** to force load the specified provider version. If the version is unavailable, then WMI returns the error 0x80041013, **wbemErrProviderLoadFailure** for Visual Basic and **WBEM\_E\_PROVIDER\_LOAD\_FAILURE** for C++. The default value for this flag when it is not specified is **FALSE**.

</dd> </dl>

On a 64-bit system that has side-by-side versions of a provider, a 32-bit application or script automatically receives data from the 32-bit provider, unless these flags are supplied and indicate that the 64-bit provider data should be returned.

## Using the Context Flags

C++ applications can use the [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) interface with [**IWbemServices::ExecMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethod) to communicate the use of a nondefault provider to WMI.

In scripting and Visual Basic, you must create a [**SWbemNamedValueSet**](swbemnamedvalueset.md) object containing the flags for the *objWbemNamedValueSet* parameter of [**SWbemServices.ExecMethod**](swbemservices-execmethod.md). For more information about setting up the parameters objects for this call, see [Constructing InParameters Objects and Parsing OutParameters Objects](constructing-inparameters-objects-and-parsing-outparameters-objects.md).

You can safely run scripts and applications using the context flags in older operating systems, because WMI ignores them in systems in which they are not implemented. While 32-bit and 64-bit versions of the System Registry provider exist, note that only one version of the WMI repository exists.

## Accessing the Default Registry Hive

The following series of examples use the [Registry Provider](/previous-versions/windows/desktop/regprov/system-registry-provider), which has side-by-side 32-bit and 64-bit versions preinstalled on 64-bit operating systems. In these examples, 32-bit clients get data returned by the provider from the 32-bit node **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Wow6432Node\\Microsoft**. 64-bit clients get data returned by the provider from the 64-bit node **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Logging**.

The scripts show how to call the methods of the Registry [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov) class through [**SWbemServices.ExecMethod**](swbemservices-execmethod.md) to obtain data from the 32-bit registry hive.

The following script gets back data from the provider that matches the bit width of the caller, in this case 64 bits, because it is a script running under the 64-bit Windows Script Host (WSH). The script gets the value from the 64-bit registry node **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\WBEM\\CIMOM\\Logging** rather than the 32-bit node **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Wow6432Node\\Microsoft\\WBEM\\CIMOM**.


```VB
strComputer = "."
Const HKLM = &h80000002
Set objReg = Getobject("winmgmts:" _
    & "{impersonationLevel=impersonate}!\\" & strComputer _
    & "\root\default:stdregprov")
'Set up inParameters object
Set Inparams = objReg.Methods_("GetStringValue").Inparameters
Inparams.Hdefkey = HKLM
Inparams.Ssubkeyname = "Software\Microsoft\Wbem\CIMOM"
Inparams.Svaluename = "Logging"
set Outparams = objReg.ExecMethod_("GetStringValue", Inparams)

'Show output parameters object and the registry value HKLM\SOFTWARE\
WScript.Echo Outparams.GetObjectText_
WScript.Echo "WMI Logging is set to  " & Outparams.SValue
```



If the **Logging** value in the default hive is set to 1, then the output from the script should look something like the following:

``` syntax
instance of __PARAMETERS
{
    ReturnValue = 0;
    sValue = "1";
};
WMI Logging is set to 1
```

## Example: Specifically Requesting the 32-bit Registry Hive on a 64-bit Computer

The following modified example of the default script uses the **\_\_ProviderArchitecture** string flag to request access to the 32-bit registry data on a 64-bit computer. The caller is connected to the 32-bit hive irrespective of whether it is a 32- or 64-bit application.


```VB
strComputer = "."
Const HKLM = &h80000002
Set objCtx = CreateObject("WbemScripting.SWbemNamedValueSet")
objCtx.Add "__ProviderArchitecture", 32
Set objLocator = CreateObject("Wbemscripting.SWbemLocator")
Set objServices = objLocator.ConnectServer(strComputer,"root\default","","",,,,objCtx)
Set objStdRegProv = objServices.Get("StdRegProv") 

Set Inparams = objStdRegProv.Methods_("GetStringValue").Inparameters
Inparams.Hdefkey = HKLM
Inparams.Ssubkeyname = "Software\Microsoft\Wbem\CIMOM"
Inparams.Svaluename = "Logging"
set Outparams = objStdRegProv.ExecMethod_("GetStringValue", Inparams,,objCtx)

'show output parameters object and the registry value HKLM\SOFTWARE\
WScript.Echo Outparams.GetObjectText_
WScript.Echo "WMI Logging is set to  " & Outparams.SValue
```



## Example: Forcing WMI to Access the 32-bit Registry Hive on a 64-bit Computer

The following modification of the script above by adding the **\_\_ProviderArchitecture** and **\_\_RequiredArchitecture** flags to the context parameter forces WMI to load the 32-bit provider and get 32-bit data. If the provider does not exist, then a provider load error occurs. The context object must be supplied in the connection to WMI by calling [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md).


```VB
strComputer = "."
Const HKLM = &h80000002
Set objCtx = CreateObject("WbemScripting.SWbemNamedValueSet")
objCtx.Add "__ProviderArchitecture", 32
objCtx.Add "__RequiredArchitecture", TRUE
Set objLocator = CreateObject("Wbemscripting.SWbemLocator")
Set objServices = objLocator.ConnectServer(strComputer,"root\default","","",,,,objCtx)
Set objStdRegProv = objServices.Get("StdRegProv") 

' Use ExecMethod to call the GetStringValue method
Set Inparams = objStdRegProv.Methods_("GetStringValue").Inparameters
Inparams.Hdefkey = HKLM
Inparams.Ssubkeyname = "Software\Microsoft\Wbem\CIMOM"
Inparams.Svaluename = "Logging"
set Outparams = objStdRegProv.ExecMethod_("GetStringValue", Inparams,,objCtx)

'Show output parameters object and the registry value HKLM\SOFTWARE\
WScript.Echo Outparams.GetObjectText_
WScript.Echo "WMI Logging is set to  " & Outparams.SValue
```



## Related topics

<dl> <dt>

[Getting and Providing Data on a 64-bit Computer](getting-and-providing-data-on-a-64-bit-computer.md)
</dt> </dl>

 

 
