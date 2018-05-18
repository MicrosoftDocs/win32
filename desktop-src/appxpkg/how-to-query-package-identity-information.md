---
title: Query app package manifest info (C++)
description: Learn how to get info from the app package manifest for a Windows Store app using the packaging API.
ms.assetid: 'A29986F9-C620-48CD-87F8-525DFA076AAB'
---

# Query app package manifest info (C++)

Learn how to get info from the app package manifest for a Windows Store app using the [packaging API](interfaces.md).

### Create a package manifest reader

To create a package manifest reader, call [**IAppxFactory::CreatePackageReader**](iappxfactory-createpackagereader.md) to create a package reader. The first parameter is an input stream for the package (.appx file). The second parameter is an output parameter that receives a pointer to an [**IAppxPackageReader**](iappxpackagereader.md) pointer. Next, call [**IAppxPackageReader::GetManifest**](iappxpackagereader-getmanifest.md) to get the manifest reader. The parameter is an output parameter that receives a pointer to an [**IAppxManifestReader**](iappxmanifestreader.md) pointer.


```C++
int wmain(
    _In_ int argc,
    _In_reads_(argc) wchar_t** argv)
{
    HRESULT hr = S_OK;
 
    if (argc != 2)
    {
        wprintf(L"Usage: DescribeAppx.exe inputFile\n");
        wprintf(L"       inputFile: Path to the app package to read\n");
        return 2;
    }

    // Specify the appropriate COM threading model
    hr = CoInitializeEx(NULL, COINIT_MULTITHREADED);

    if (SUCCEEDED(hr))
    {
        IAppxPackageReader* packageReader = NULL;
        IAppxManifestReader* manifestReader = NULL;

        // Create a package reader using the file name given in command line
        hr = GetPackageReader(argv[1], &amp;packageReader);

        // Get manifest reader for the package and read from the manifest
        if (SUCCEEDED(hr))
        {
            hr = packageReader->GetManifest(&amp;manifestReader);
        }
        if (SUCCEEDED(hr))
        {
            hr = ReadManifest(manifestReader);
        }
    }
}

//
// Creates an app package reader.
//
// Parameters:
//   inputFileName 
//     Fully qualified name of the app package (.appx file) to be opened.
//   reader 
//     On success, receives the created instance of IAppxPackageReader.
//
HRESULT GetPackageReader(
    _In_ LPCWSTR inputFileName,
    _Outptr_ IAppxPackageReader** reader)
{
    HRESULT hr = S_OK;
    IAppxFactory* appxFactory = NULL;
    IStream* inputStream = NULL;

    // Create a new factory
    hr = CoCreateInstance(
            __uuidof(AppxFactory),
            NULL,
            CLSCTX_INPROC_SERVER,
            __uuidof(IAppxFactory),
            (LPVOID*)(&amp;appxFactory));

    // Create a stream over the input app package
    if (SUCCEEDED(hr))
    {
        hr = SHCreateStreamOnFileEx(
                inputFileName,
                STGM_READ | STGM_SHARE_EXCLUSIVE,
                0, // default file attributes
                FALSE, // do not create new file
                NULL, // no template
                &amp;inputStream);
    }

    // Create a new package reader using the factory.  For 
    // simplicity, we don't verify the digital signature of the package.
    if (SUCCEEDED(hr))
    {
        hr = appxFactory->CreatePackageReader(
                inputStream,
                reader);
    }

    // Clean up allocated resources
    if (inputStream != NULL)
    {
        inputStream->Release();
        inputStream = NULL;
    }
    if (appxFactory != NULL)
    {
        appxFactory->Release();
        appxFactory = NULL;
    }
    return hr;
}
```



### Read package identity info

Package identify is specified using the [**Identity**](https://msdn.microsoft.com/library/windows/apps/br211441) element in the manifest. Use [**IAppxManifestReader::GetPackageId**](iappxmanifestreader-getpackageid.md) to get an [**IAppxManifestPackageId**](iappxmanifestpackageid.md) to read package identity info, as shown here.

This code uses [**IAppxManifestPackageId::GetPackageFullName**](iappxmanifestpackageid-getpackagefullname.md) to get the package full name, [**IAppxManifestPackageId::GetName**](iappxmanifestpackageid-getname.md) to get the package name, and [**IAppxManifestPackageId::GetVersion**](iappxmanifestpackageid-getversion.md) to get the package version.


```C++
//
// Reads a subset of the manifest Identity element.
//
//
HRESULT ReadManifestPackageId(
    _In_ IAppxManifestReader* manifestReader)
{
    HRESULT hr = S_OK;

    IAppxManifestPackageId* packageId = NULL;

    // Get elements and attributes from the manifest reader
    hr = manifestReader->GetPackageId(&amp;packageId);
    if (SUCCEEDED(hr))
    {
        LPWSTR packageFullName = NULL;
        LPWSTR packageName = NULL;
        UINT64 packageVersion = 0;

        hr = packageId->GetPackageFullName(&amp;packageFullName);

        if (SUCCEEDED(hr))
        {
            hr = packageId->GetName(&amp;packageName);
        }
        if (SUCCEEDED(hr))
        {
            hr = packageId->GetVersion(&amp;packageVersion);
        }
        if (SUCCEEDED(hr))
        {
            wprintf(L"Package full name: %s\n", packageFullName);
            wprintf(L"Package name: %s\n", packageName);
            wprintf(L"Package version: ");

            // Convert version number from 64-bit integer to dot-quad form
            for (int bitPosition = 0x30; bitPosition >= 0; bitPosition -= 0x10)
            {
                UINT64 versionWord = (packageVersion >> bitPosition) & 0xFFFF;
                wprintf(L"%llu.", versionWord);
            }
            wprintf(L"\n");
        }

        // Free all string buffers returned from the manifest API
        CoTaskMemFree(packageFullName);
        CoTaskMemFree(packageName);
    }

    // Clean up allocated resources
    if (packageId != NULL)
    {
        packageId->Release();
        packageId = NULL;
    }
     
    return hr;
}
```



### Read metadata that describes the package to users

Properties are specified using the [**Properties**](https://msdn.microsoft.com/library/windows/apps/br211457) element in the manifest. Use [**IAppxManifestReader::GetProperties**](iappxmanifestreader-getproperties.md) to get an [**IAppxManifestProperties**](iappxmanifestproperties.md) to read this node, as shown here.

This code uses [**IAppxManifestProperties::GetStringValue**](iappxmanifestproperties-getstringvalue.md) to get the package display name and package description.


```C++
//
// Reads a subset of the manifest Properties element.
//
//
HRESULT ReadManifestProperties(
    _In_ IAppxManifestReader* manifestReader)
{
    HRESULT hr = S_OK;

    IAppxManifestProperties* properties = NULL;

    // Get elements and attributes from the manifest reader
    hr = manifestReader->GetProperties(&amp;properties);
    if (SUCCEEDED(hr))
    {
        LPWSTR displayName = NULL;
        LPWSTR description = NULL;

        hr = properties->GetStringValue(L"DisplayName", &amp;displayName);

        if (SUCCEEDED(hr))
        {
            hr = properties->GetStringValue(L"Description", &amp;description);
        }
        if (SUCCEEDED(hr))
        {
            wprintf(L"Package display name: %s\n", displayName);
            wprintf(L"Package description:  %s\n", description);
        }

        // Free all string buffers returned from the manifest API
        CoTaskMemFree(displayName);
        CoTaskMemFree(description);
    }
    // Clean up allocated resources
    if (properties != NULL)
    {
        properties->Release();
        properties = NULL;
    }

    return hr;
}
```



### Read metadata about the apps included in the package

Apps are specified using the [**Applications**](https://msdn.microsoft.com/library/windows/apps/br211417) element in the manifest. Use [**IAppxManifestReader::GetApplications**](iappxmanifestreader-getapplications.md) to get an [**IAppxManifestApplicationsEnumerator**](iappxmanifestapplicationsenumerator.md) to read this node. Use [**IAppxManifestApplicationsEnumerator::GetCurrent**](iappxmanifestapplicationsenumerator-getcurrent.md) and [**IAppxManifestApplicationsEnumerator::MoveNext**](iappxmanifestapplicationsenumerator-movenext.md) to get an [**IAppxManifestApplication**](iappxmanifestapplication.md) for each app in the package.

This code uses [**IAppxManifestApplication::GetStringValue**](iappxmanifestapplication-getstringvalue.md) to get the display name for each app.


```C++
//
// Reads a subset of the manifest Applications element.
//
//
HRESULT ReadManifestApplications(
    _In_ IAppxManifestReader* manifestReader)
{
    HRESULT hr = S_OK;
    BOOL hasCurrent = FALSE;
    UINT32 applicationsCount = 0;

    IAppxManifestApplicationsEnumerator* applications = NULL;

    // Get elements and attributes from the manifest reader
    hr = manifestReader->GetApplications(&amp;applications);
    if (SUCCEEDED(hr))
    {
        hr = applications->GetHasCurrent(&amp;hasCurrent);

        while (SUCCEEDED(hr) &amp;&amp; hasCurrent)
        {
            IAppxManifestApplication* application = NULL;
            LPWSTR applicationName = NULL;

            hr = applications->GetCurrent(&amp;application);
            if (SUCCEEDED(hr))
            {
                application->GetStringValue(L"DisplayName", &amp;applicationName);
            }
            if (SUCCEEDED(hr))
            {
                applicationsCount++;
                wprintf(L"App #%u: %s\n", applicationsCount, applicationName);
            }

            if (SUCCEEDED(hr))
            {
                hr = applications->MoveNext(&amp;hasCurrent);
            }
            if (application != NULL)
            {
                application->Release();
                application = NULL;
            }
            CoTaskMemFree(applicationName);
        }

        wprintf(L"Count of apps in the package: %u\n", applicationsCount);
    }

    // Clean up allocated resources
    if (applications != NULL)
    {
        applications->Release();
        applications = NULL;
    }

    return hr;
}
```



### Clean up the package manifest reader

Before returning from the `wmain` function, call the [**Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317) method to clean up the package manifest reader and call the [**CoUninitialize**](https://msdn.microsoft.com/library/windows/desktop/ms688715) function.


```C++
// Clean up allocated resources
if (manifestReader != NULL)
{
    manifestReader->Release();
    manifestReader = NULL;
}
if (packageReader != NULL)
{
    packageReader->Release();
    packageReader = NULL;
}

CoUninitialize();
```



## Related topics

<dl> <dt>

**Samples**
</dt> <dt>

[Query app package and app manifest sample](http://go.microsoft.com/fwlink/p/?linkid=236966)
</dt> <dt>

**Reference**
</dt> <dt>

[**IAppxManifestReader**](iappxmanifestreader.md)
</dt> </dl>

 

 




