---
title: Using BITS from .NET using Reference DLLs
description: The following examples show how to call into the BITS COM interface from a .NET program
ms.assetid: 1058970C-CE81-47D6-950E-3B6289E956B6
ms.topic: article
ms.date: 11/13/2018
---

# Calling into BITS from .NET and C# using Reference DLLs

One way to call into the BITS COM classes from a .NET program is to create a reference DLL file starting with the BITS [IDL](/windows/desktop/Midl/midl-start-page) (Interface Definition Language) files in the Windows SDK, using the [MIDL](/windows/desktop/Midl/using-the-midl-compiler-2) and [TLBIMP](/dotnet/framework/tools/tlbimp-exe-type-library-importer) tools. The reference DLL is a set of class wrappers for the BITS COM classes; you can then use the wrapper classes directly from .NET.

An alternative to using automatically-created reference DLLs is to use a 3rd party .NET BITS wrapper from [GitHub](https://github.com/) and [NuGet](https://www.nuget.org/). These wrappers often have a more natural .NET programming style but they might lag behind the changes and updates in the BITS interfaces.

## Creating the reference DLLs
### BITS IDL files

You will start with the set of BITS IDL files. These are files that fully define the BITS COM interface. The files are located in the **Windows Kits** directory and are named bits*version*.idl (for example, bits10_2.idl) except for the version 1.0 file which is just Bits.idl. As new versions of BITS are created, new BITS IDL files are also created.

You may also want to modify a copy of the SDK BITS IDL files to use BITS features that aren't automatically converted into .NET equivalents. Possible IDL file changes are discussed later on.

The BITS IDL files include several other IDL files by reference. They also nest, so that if you use one version, it includes all the lower versions.

For each version of BITS that you want to target in your program you will need one reference DLL for that version. For example, if you want to write a program that works on BITS 1.5 and up but has additional features when BITS 10.2 is present, you need to convert both the bits1_5.idl and bits10_2.idl files.


### MIDL and TLBIMP utilities

The [MIDL](/windows/desktop/Midl/using-the-midl-compiler-2) (Microsoft Interface Definition Language) utility converts the IDL files that describe the BITS COM interface into a TLB (Type Library) file. The MIDL tool depends on the CL utility (C preprocessor) to correctly read the IDL language file. The CL utility is part of Visual Studio and is installed when you include C/C++ features in the Visual Studio installation.

The MIDL utility will normally create a set of C and H (C language code and C language header) files. You can suppress these extra files by sending the output to the NUL: device. For example, setting the /dlldata NUL: switch will suppress creating a dlldata.c file. The sample commands below shows which switches should be set to NUL:.

The [TLBIMP](/dotnet/framework/tools/tlbimp-exe-type-library-importer) (Type Library Importer) utility reads in a TLB file and creates the corresponding reference DLL file. 


### Example commands for MIDL and TLBIMP

This is an example of the complete set of commands to generate a set of reference files. You may need to modify the commands based on your Visual Studio and Windows SDK installation and based on the BITS features and OS versions you are targeting. 

The example creates a directory to place the reference DLL files and creates an environment variable BITSTEMP to point to that directory. 

The example commands then run the vsdevcmd.bat file that's created by the Visual Studio installer. This BAT file will set up your paths and some environment variables so that the MIDL and TLBIMP commands will run. It also sets up the WindowsSdkDir and WindowsSDKLibVersion variables to point to the most recent Windows SDK directories.

```console
REM Create a working directory
REM You can select a different directory based on your needs.
SET BITSTEMP=C:\BITSTEMPDIR
MKDIR "%BITSTEMP%"

REM Run the VsDevCmd.bat file to locate the Windows
REM SDK directory and the tools directories
REM This will be different for different versions of
REM Visual Studio

CALL "C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\Common7\Tools\vsdevcmd.bat"

REM Run the MIDL command on the desired BITS IDL file
REM This will generate a TLB file for the TLBIMP command
REM The IDL file will be different depending on which
REM set of BITS interfaces you need to use.
REM Run the MIDL command once per reference file
REM that you will need to explicitly use.
PUSHD .
CD /D "%WindowsSdkDir%Include\%WindowsSDKLibVersion%um"

MIDL  /I ..\shared /out "%BITSTEMP%" bits1_5.idl /dlldata NUL: /header NUL: /iid NUL: /proxy NUL:
MIDL  /I ..\shared /out "%BITSTEMP%" bits4_0.idl /dlldata NUL: /header NUL: /iid NUL: /proxy NUL:
MIDL  /I ..\shared /out "%BITSTEMP%" bits5_0.idl /dlldata NUL: /header NUL: /iid NUL: /proxy NUL:
MIDL  /I ..\shared /out "%BITSTEMP%" bits10_1.idl /dlldata NUL: /header NUL: /iid NUL: /proxy NUL:
MIDL  /I ..\shared /out "%BITSTEMP%" bits10_2.idl /dlldata NUL: /header NUL: /iid NUL: /proxy NUL:

REM Run the TLBIMP command on the resulting TLB file(s)
REM Try to keep a parallel set of names.
TLBIMP "%BITSTEMP%"\bits1_5.tlb /out: "%BITSTEMP%"\BITSReference1_5.dll
TLBIMP "%BITSTEMP%"\bits4_0.tlb /out: "%BITSTEMP%"\BITSReference4_0.dll
TLBIMP "%BITSTEMP%"\bits5_0.tlb /out: "%BITSTEMP%"\BITSReference5_0.dll
TLBIMP "%BITSTEMP%"\bits10_1.tlb /out: "%BITSTEMP%"\BITSReference10_1.dll
TLBIMP "%BITSTEMP%"\bits10_2.tlb /out: "%BITSTEMP%"\BITSReference10_2.dll
DEL "%BITSTEMP%"\bits*.tlb
POPD

```
Once these commands are run you will have a set of reference DLLs in the BITSTEMP directory.

### Adding the reference DLLs to your project

To use a reference DLL in a C# project, open your C# project in Visual Studio. In the Solution Explorer, right-click the References and click Add Reference. Then click the Browse button and then the Add button. Navigate to the directory with the reference DLLs, select them, and click Add. In the Reference Manager window the reference DLLs will be checked. Then click OK.

The BITS reference DLLs are now added to your project.

The information in the reference DLL files will be embedded into your final program. You do not have to ship the reference DLL files with your program; you just need to ship the .EXE. 

You can change whether the reference DLLs are embedded into the final EXE. Use the [Embed Interop Types](/dotnet/framework/interop/how-to-add-references-to-type-libraries) property to set whether or not the reference DLLs will be embedded. This can be done on a per-reference basis. The default is True to embed the DLLs.

## Modifying IDL files for more complete .NET code

The BITS IDL (Microsoft Interface Definition Language) files can be used unchanged to make the BackgroundCopyManager DLL file. However, the resulting .NET reference DLL will be missing some untranslatable unions and has hard-to-use names for some structures and enums. This section will describe some of the changes that you can make to make the .NET DLL more complete and easier to use.

### Simpler ENUM names

The BITS IDL files typically define enum values like this:
```
    typedef enum
    {
            BG_AUTH_TARGET_SERVER = 1,
            BG_AUTH_TARGET_PROXY
    } BG_AUTH_TARGET;
```
The BG_AUTH_TARGET is the name of the typedef; the actual enum is not named. This doesn’t typically cause problems with C code but doesn’t translate well for use with a .NET program. A new name will be automatically created, but it might look something like _MIDL___MIDL_itf_bits4_0_0005_0001_0001 instead of a human-readable value. You can fix this problem by updating the MIDL files to include an enum name.

```
    typedef enum BG_AUTH_TARGET
    {
            BG_AUTH_TARGET_SERVER = 1,
            BG_AUTH_TARGET_PROXY
    } BG_AUTH_TARGET;
```

The enum name is allowed to be the same as the typedef name. Some programmers have a naming convention where they are kept different (for example, by putting an underscore before the enum name), but this will only confuse the .NET translations. 

### String types in unions

The BITS IDL files pass strings using the LPWSTR (long pointer to wide-character string) convention. Although this works when passing function parameters (like the Job.GetDisplayName([out] LPWSTR *pVal) method), it doesn’t work when the strings are part of unions. For example, the bits5_0.idl file includes the BITS_FILE_PROPERTY_VALUE union:

```
typedef [switch_type(BITS_FILE_PROPERTY_ID)] union
{
    [case( BITS_FILE_PROPERTY_ID_HTTP_RESPONSE_HEADERS )]
        LPWSTR String;
}
BITS_FILE_PROPERTY_VALUE;
```

The LPWSTR field won’t be included in the .NET version of the union. To fix this, change the LPWSTR to a WCHAR*. The resulting field (called String) will be passed as a IntPtr. Convert this into a string using the  System.Runtime.InteropServices.Marshal.PtrToStringAuto(value.String); method.

### Unions in structures

Sometimes unions that are embedded in structures won't be included in the structure at all. For example, in the Bits1_5.idl the BG_AUTH_CREDENTIALS is defined as follows:
```
    typedef struct
    {
        BG_AUTH_TARGET Target;
        BG_AUTH_SCHEME Scheme;
        [switch_is(Scheme)] BG_AUTH_CREDENTIALS_UNION Credentials;
    }
    BG_AUTH_CREDENTIALS;
```

The BG_AUTH_CREDENTIALS_UNION is defined to be a union as follows:
```
    typedef [switch_type(BG_AUTH_SCHEME)] union
    {
            [case( BG_AUTH_SCHEME_BASIC, BG_AUTH_SCHEME_DIGEST, BG_AUTH_SCHEME_NTLM,
            BG_AUTH_SCHEME_NEGOTIATE, BG_AUTH_SCHEME_PASSPORT )] BG_BASIC_CREDENTIALS Basic;
            [default] ;
    } BG_AUTH_CREDENTIALS_UNION;
```
The Credentials field in the BG_AUTH_CREDENTIALS will not be included in the .NET class definition.

Note that the union is defined to always be a BG_BASIC_CREDENTIALS regardless of the BG_AUTH_SCHEME. Because the union isn’t used as a union, we can just pass a BG_BASIC_CREDENTIALS like this:
```
    typedef struct
    {
        BG_AUTH_TARGET Target;
        BG_AUTH_SCHEME Scheme;
        BG_BASIC_CREDENTIALS Credentials;
    }
    BG_AUTH_CREDENTIALS;
```

## Using BITS from C#

### Recommended using statement

Setting up some using statements in C# will reduce the number of characters you need to type to use the different BITS versions. The name "BITSReference" comes from the name of the reference DLL.

```csharp
// Set up the BITS namespaces
using BITS = BITSReference1_5;
using BITS4 = BITSReference4_0;
using BITS5 = BITSReference5_0;
using BITS10_2 = BITSReference10_2;
```

### Quick Sample: download a file

A short but complete snippet of C# code to download a file from a URL is given below. 

```csharp
    var mgr = new BITS.BackgroundCopyManager1_5();
    BITS.GUID jobGuid;
    BITS.IBackgroundCopyJob job;
    mgr.CreateJob("Quick download", BITS.BG_JOB_TYPE.BG_JOB_TYPE_DOWNLOAD, out jobGuid, out job);
    job.AddFile("https://aka.ms/WinServ16/StndPDF", @"C:\Server2016.pdf");
    job.Resume();
    bool jobIsFinal = false;
    while (!jobIsFinal)
    {
        BITS.BG_JOB_STATE state;
        job.GetState(out state);
        switch (state)
        {
            case BITS.BG_JOB_STATE.BG_JOB_STATE_ERROR:
            case BITS.BG_JOB_STATE.BG_JOB_STATE_TRANSFERRED:
                job.Complete();
                break;

            case BITS.BG_JOB_STATE.BG_JOB_STATE_CANCELLED:
            case BITS.BG_JOB_STATE.BG_JOB_STATE_ACKNOWLEDGED:
                jobIsFinal = true;
                break;
            default:
                Task.Delay(500); // delay a little bit
                break;
        }
    }
    // Job is complete
```

In this sample code, a BITS manager named mgr is created. It directly corresponds to the [IBackgroundCopyManager](/windows/desktop/api/bits/nn-bits-ibackgroundcopymanager) interface. 

From the manager a new job is created. The job is an out parameter on the CreateJob method. Also passed in is the job name (which doesn't have to be unique) and the download type, which is a download job. A BITS GUID for the job identifier is also filled in.

Once the job is created you add a new download file to the job with the AddFile method. You need to pass in two strings, one for the remote file (the URL or file share) and one for the local file. 

After adding the file, call Resume on the job to start it. Then the code waits until the job is in a final state (ERROR or TRANSFERRED) and is then completed.

### BITS Versions, Casting and QueryInterface

You'll find that you often have to use both an early version of a BITS object and a more recent version in your program.  

For example, when you make a job object, you will get an IBackgroundCopyJob (part of BITS version 1.0) even when you're making it using a more recent manager object and a more recent IBackgroundCopyJob object is available. Because the CreateJob method doesn't accept an interface for the more recent version, you can't directly make the more recent version.

Use a .NET cast to convert from an older type object to a newer type object. The cast will automatically call a COM QueryInterface as appropriate. 

In this example, there's a BITS IBackgroundCopyJob object named "job", and we want to convert it to an IBackgroundCopyJob5 object named "job5" so that we can call the BITS 5.0 GetProperty method. We just cast to the IBackgroundCopyJob5 type like this:

```csharp
var job5 = (BITS5.IBackgroundCopyJob5)job;
```

The job5 variable will be initialized by .NET by using the correct QueryInterface. 

If your code might run on a system that doesn't support a particular version of BITS, you can try the cast and catch the System.InvalidCastException. 

```csharp
BITS5.IBackgroundCopyJob5 job5 = null;
try
{
    job5 = (BITS5.IBackgroundCopyJob5)Job;
}
catch (System.InvalidCastException)
{
    ; // Must be running an earlier version of BITS
}
```

A common problem is when you try to cast into the wrong kind of object. The .NET system doesn't know about the real relationship between the BITS interfaces. If you ask for the wrong kind of interface, .NET will try to make it for you and will fail with an InvalidCastException and HResult 0x80004002 (E_NOINTERFACE).

### Working with BITS Versions 10_1 and 10_2

On some versions of Windows 10 you can't directly create a BITS IBackgroundCopyManager object using the 10.1 or 10.2 interfaces. Instead, you'll have to use multiple versions of the BackgroundCopyManager DLL reference files. For example, you can use the 1.5 version to make an IBackgroundCopyManager object, and then cast the resulting job or file objects using the 10.1 or 10.2 versions.

