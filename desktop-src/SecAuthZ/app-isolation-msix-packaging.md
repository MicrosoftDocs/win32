---
title: Packaging an isolated Win32 app with MSIX
description: Packaging an existing MSIX or Win32 application into a Win32 app isolation application will be done through the MSIX Packaging Tool (MPT).
ms.topic: article
ms.date: 08/26/2024
---

# Packaging an isolated Win32 app with MSIX

Packaging an existing MSIX or Win32 application into a Win32 app isolation application will be done through the MSIX Packaging Tool (MPT). Note that the version of MPT that supports Win32 app isolation is v1.2023.517.0, available in the release assets of this project. The [store version of MPT](/windows/msix/packaging-tool/tool-overview) is outdated for the purposes of the Win32 app isolation feature. You can find additional documentation for MPT [here](/windows/msix/packaging-tool/tool-overview).

You can find the download for MPT, as well as the profiler, in the [releases](https://github.com/microsoft/win32-app-isolation/releases) section of the Win32 app isolation GitHub repository.

> [!IMPORTANT]
> **This feature is in preview:** Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

## Convert an existing Win32 installer into an MSIX app

1. Select "Application Package" on the far left and choose where the package will be created. This flow will follow the "Create package on this computer" option.

   > [!NOTE]
   > This will result in the app installed as a normal Win32 app after finishing step 5.

   :::image type="content" source="images/app-isolation/01-packaging-main-menu.png" alt-text="A screenshot showing the main page of the MSIX Packaging Tool":::

1. Wait for the "MSIX Packaging Tool Driver" field to finish checking.

   :::image type="content" source="images/app-isolation/02-packaging-prepare.png" alt-text="A screenshot showing the Create New Package page of the MSIX Packaging Tool":::

1. Use the browse button to navigate to and select the Win32 installer. Leave signing preference blank as we will need to edit the manifest and sign it again.

   :::image type="content" source="images/app-isolation/03-packaging-installer.png" alt-text="A screenshot showing the Select Installer page in the MSIX Packaging Tool":::

1. Enter the package information.

   :::image type="content" source="images/app-isolation/04-packaging-package-info.png" alt-text="A screenshot showing the Package Information page in the MSIX Packaging Tool":::

1. Go through the Win32 installer as normal

1. If there are additional entry points besides the main one, launch or browse to them. If the app has options for File Type Association in settings/config/preferences, toggle them at this step so MSIX will pick up on them.

1. Repeat the same process if there are services in the package.

1. Clicking Create will save the package as a full trust package. Click the "Package Editor" button to go to the "Package Editor" flow from the main menu. This can take up to several minutes depending on the size of the package.

   :::image type="content" source="images/app-isolation/05-packaging-create-package.png" alt-text="A screenshot showing the final Create Package page when creating a package in the MSIX Packaging Tool":::

## Convert an existing MSIX app to run isolated

1. Select the far right option "Package editor" and browse to the .msix file and click the "Open package" button.

   :::image type="content" source="images/app-isolation/01-packaging-main-menu.png" alt-text="A screenshot showing the main page before clicking Open Package in the MSIX Packaging Tool":::

1. Scroll down to the "Manifest file" section and click "Open file".

   :::image type="content" source="images/app-isolation/10-packaging-package-editor.png" alt-text="A screenshot showing the Package Information page after clicking Open Package in the MSIX Packaging Tool":::

   In the manifest, the following changes will need to be made.

   > [!NOTE]
   > Isolated Win32 applications are not compatible with other application types within the same package.

   - Add `xmlns:previewsecurity2="http://schemas.microsoft.com/appx/manifest/preview/windows10/security/2"` to the `<Package>` element if it's not there already.
     - Add `previewsecurity2` to `IgnorableNamespaces` at the end of the `<Package>` element.
   - Add `xmlns:uap10="http://schemas.microsoft.com/appx/manifest/uap/windows10/10"` to the `<Package>` element if it's not there already.
     - Add `uap10` to `IgnorableNamespaces` at the end of the `<Package>` element.
   - In `<Dependencies>` change `TargetDeviceFamily` to `<TargetDeviceFamily Name="Windows.Desktop" MinVersion="10.0.25357.0" MaxVersionTested="10.0.25357.0" />`.
     > [!NOTE]
     > Not all features are available in the minimum build, check out the [release notes](https://github.com/microsoft/win32-app-isolation/blob/main/relnotes/windows-release-notes.md) for more detailed information.
   - In `<Application>` replace any existing entrypoint/trustlevel/runtimebehavior with `uap10:TrustLevel="appContainer" previewsecurity2:RuntimeBehavior="appSilo"`.
   - In `<Application>` extensions, remove any `EntryPoints=*` or `Executable=*` as those are inherited from the parent `<Application>`
   - Add `desktop7:Scope="user"` to the extension element for `windows.protocol`.

   > [!NOTE]
   > By default, MPT will automatically add `<rescap:Capability name="runFullTrust">` to `<Capabilities>` due to the app being a packaged Win32. This should be removed unless the app has other manifested extensions which can affect the user global state, such as `comServer` or `FirewallRules`, since those require the `runFullTrust` capability.

   :::image type="content" source="images/app-isolation/11-packaging-manifest.png" alt-text="A screenshot showing the app manifest file contents":::

1. The app might need additional capabilities to function correctly now that it has been isolated.

   These capabilities directly add functionality back to isolated apps.

   - `isolatedWin32-print` - Print documents
   - `isolatedWin32-sysTrayIcon` - Display notifications from the Systray
   - `isolatedWin32-shellExtensionContextMenu` - Display COM-based context menu entries
   - `isolatedWin32-promptForAccess` - Prompt Users for file access
   - `isolatedWin32-accessToPublisherDirectory` - Access to directories that end with the publisher ID

   These capabilities allow minimal access to libraries such as MSVC runtime or other Windows/3rd Party DLLs for applications that don't support prompting.

   - `isolatedWin32-dotNetBreadcrumbStore`
   - `isolatedWin32-profilesRootMinimal`
   - `isolatedWin32-userProfileMinimal`
   - `isolatedWin32-volumeRootMinimal`

1. Save and close the manifest window. If there are any errors in the manifest, MPT will display them. Select Create/Save to generate the .msix file. This can take several minutes depending on the size of the package

   - If there are errors with the manifest, a more actionable error message can be found in Event Viewer under `Application and Services/Microsoft/Windows/AppxPackagingOM/Microsoft-Windows-AppxPackaging/Operational`

1. See [application capability profiler](app-isolation-capability-profiler.md) for information on identifying capabilities that may need to be declared in the application package manifest.

## Related topics

[Win32 app isolation overview](app-isolation-overview.md)

[Application Capability Profiler](app-isolation-capability-profiler.md)

[Packaging a Win32 app isolation application with Visual Studio](app-isolation-packaging-with-vs.md)
