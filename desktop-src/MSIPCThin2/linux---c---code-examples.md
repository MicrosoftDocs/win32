---
title: Linux code examples
description: This topic introduces you to important scenarios and code elements for the Linux version of the RMS SDK.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 0F7714CA-1D3E-4846-B187-739825B7DE26
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Linux code examples

This topic introduces you to important scenarios and code elements for the Linux version of the RMS SDK.

The code snippets below are from the sample applications, *rms\_sample* and *rmsauth\_sample*. For more information, see [samples](https://github.com/AzureAD/rms-sdk-for-cpp/tree/master/samples) at the GitHub repository.

-   [**Scenario**: Access protection policy information from a protected file](#scenario-access-protection-policy-information-from-a-protected-file)
-   [**Scenario**: Create a new protected file using a template](#scenario-create-a-new-protected-file-using-a-template)
-   [**Scenario**: Protect a file using custom protection](#scenario-protect-a-file-using-custom-protection)
-   [WorkerThread - a supporting method](#workerthread---a-supporting-method)
-   [**Scenario**: RMS authentication](#scenario-rms-authentication)

## **Scenario**: Access protection policy information from a protected file

<dl> **Opens and reads an RMS protected fileSource**: [rms\_sample/mainwindow.cpp](https://github.com/AzureAD/rms-sdk-for-cpp/tree/master/samples/rms_sample)  
**Description**: After getting a file name from the user, reading the certificates (see *MainWindow::addCertificates*), setting up the authorization callback with Client ID and Redirect URL, calling *ConvertFromPFile* (see following code example), then reading out the protection policy name, description and content validity date.  


```C++
void MainWindow::ConvertFromPFILE(const string&amp; fileIn,
                                  const string&amp; clientId,
                                  const string&amp; redirectUrl,
                                  const string&amp; clientEmail) 
{
  // add trusted certificates using HttpHelpers of RMS and Auth SDKs
  addCertificates();

  // create shared in/out streams
  auto inFile = make_shared<ifstream>(
    fileIn, ios_base::in | ios_base::binary);

  if (!inFile->is_open()) {
    AddLog("ERROR: Failed to open ", fileIn.c_str());
    return;
  }

  string fileOut;

  // generate output filename
  auto pos = fileIn.find_last_of('.');

  if (pos != string::npos) {
    fileOut = fileIn.substr(0, pos);
  }

  // create streams
  auto outFile = make_shared<fstream>(
    fileOut, ios_base::in | ios_base::out | ios_base::trunc | ios_base::binary);

  if (!outFile->is_open()) {
    AddLog("ERROR: Failed to open ", fileOut.c_str());
    return;
  }

  try
  {
    // create authentication context
    AuthCallback auth(clientId, redirectUrl);

    // process convertion
    auto pfs = PFileConverter::ConvertFromPFile(
      clientEmail,
      inFile,
      outFile,
      auth,
      this->consent);

    AddLog("Successfully converted to ", fileOut.c_str());
  }
  catch (const rmsauth::Exception&amp; e)
  {
    AddLog("ERROR: ", e.error().c_str());
  }
  catch (const rmscore::exceptions::RMSException&amp; e) {
    AddLog("ERROR: ", e.what());
  }
  inFile->close();
  outFile->close();
}
```



**Create a protected file streamSource**: [rms\_sample/pfileconverter.cpp](https://github.com/AzureAD/rms-sdk-for-cpp/tree/master/samples/rms_sample)  
**Description**: This method creates a protected file stream from the passed in backing stream through the SDK method, *ProtectedFileStream::Aquire*, which is then returned to the caller.  


```C++
shared_ptr<GetProtectedFileStreamResult>PFileConverter::ConvertFromPFile(
  const string           & userId,
  shared_ptr<istream>      inStream,
  shared_ptr<iostream>     outStream,
  IAuthenticationCallback&amp; auth,
  IConsentCallback       & consent)
{
  auto inIStream = rmscrypto::api::CreateStreamFromStdStream(inStream);

  auto fsResult = ProtectedFileStream::Acquire(
    inIStream,
    userId,
    auth,
    consent,
    POL_None,
    static_cast<ResponseCacheFlags>(RESPONSE_CACHE_INMEMORY
                                    | RESPONSE_CACHE_ONDISK));

  if ((fsResult.get() != nullptr) &amp;&amp; (fsResult->m_status == Success) &amp;&amp;
      (fsResult->m_stream != nullptr)) {
    auto pfs = fsResult->m_stream;

    // preparing
    readPosition  = 0;
    writePosition = 0;
    totalSize     = pfs->Size();

    // start threads
    for (size_t i = 0; i < THREADS_NUM; ++i) {
      threadPool.push_back(thread(WorkerThread,
                                  static_pointer_cast<iostream>(outStream), pfs,
                                  false));
    }

    for (thread&amp; t: threadPool) {
      if (t.joinable()) {
        t.join();
      }
    }
  }
  return fsResult;
}
```



</dl>

## **Scenario**: Create a new protected file using a template

<dl> <dl> **Protects a file with a user selected templateSource**: [rms\_sample/mainwindow.cpp](https://github.com/AzureAD/rms-sdk-for-cpp/tree/master/samples/rms_sample)  
**Description**: After getting a file name from the user, reading the certificates (see *MainWindow::addCertificates*) and setting up the authorization callback with Client ID and Redirect URL, the selected file is protected by calling *ConvertToPFileTemplates* (see following code example).  


```C++
void MainWindow::ConvertToPFILEUsingTemplates(const string&amp; fileIn,
                                              const string&amp; clientId,
                                              const string&amp; redirectUrl,
                                              const string&amp; clientEmail) 
{
  // generate output filename
  string fileOut = fileIn + ".pfile";

  // add trusted certificates using HttpHelpers of RMS and Auth SDKs
  addCertificates();

  // create shared in/out streams
  auto inFile = make_shared<ifstream>(
    fileIn, ios_base::in | ios_base::binary);
  auto outFile = make_shared<fstream>(
    fileOut, ios_base::in | ios_base::out | ios_base::trunc | ios_base::binary);

  if (!inFile->is_open()) {
    AddLog("ERROR: Failed to open ", fileIn.c_str());
    return;
  }

  if (!outFile->is_open()) {
    AddLog("ERROR: Failed to open ", fileOut.c_str());
    return;
  }

  // find file extension
  string fileExt;
  auto   pos = fileIn.find_last_of('.');

  if (pos != string::npos) {
    fileExt = fileIn.substr(pos);
  }

  try {
    // create authentication callback
    AuthCallback auth(clientId, redirectUrl);

    // process convertion
    PFileConverter::ConvertToPFileTemplates(
      clientEmail, inFile, fileExt, outFile, auth,
      this->consent, this->templates);

    AddLog("Successfully converted to ", fileOut.c_str());
  }
  catch (const rmsauth::Exception&amp; e) {
    AddLog("ERROR: ", e.error().c_str());
    outFile->close();
    remove(fileOut.c_str());
  }
  catch (const rmscore::exceptions::RMSException&amp; e) {
    AddLog("ERROR: ", e.what());

    outFile->close();
    remove(fileOut.c_str());
  }
  inFile->close();
  outFile->close();
}
```



**Protects a file using a policy created from a templateSource**: [rms\_sample/pfileconverter.cpp](https://github.com/AzureAD/rms-sdk-for-cpp/tree/master/samples/rms_sample)  
**Description**: A list of templates associated with the user is fetched and selected template is then used to create a policy which in turn is used to protect the file.  


```C++
void PFileConverter::ConvertToPFileTemplates(const string           & userId,
                                             shared_ptr<istream>      inStream,
                                             const string           & fileExt,
                                             std::shared_ptr<iostream>outStream,
                                             IAuthenticationCallback&amp; auth,
                                             IConsentCallback&amp; /*consent*/,
                                             ITemplatesCallback     & templ)
{
  auto templates = TemplateDescriptor::GetTemplateList(userId, auth);

  rmscore::modernapi::AppDataHashMap signedData;

  size_t pos = templ.SelectTemplate(templates);

  if (pos < templates.size()) {
    auto policy = UserPolicy::CreateFromTemplateDescriptor(
      templates[pos],
      userId,
      auth,
      USER_AllowAuditedExtraction,
      signedData);

    ConvertToPFileUsingPolicy(policy, inStream, fileExt, outStream);
  }
}
```



**Protects a file given a policySource**: [rms\_sample/pfileconverter.cpp](https://github.com/AzureAD/rms-sdk-for-cpp/tree/master/samples/rms_sample)  
**Description**: Create a protected file stream using the given policy then protect that file.  


```C++
void PFileConverter::ConvertToPFileUsingPolicy(shared_ptr<UserPolicy>   policy,
                                               shared_ptr<istream>      inStream,
                                               const string           & fileExt,
                                               std::shared_ptr<iostream>outStream)
{
  if (policy.get() != nullptr) {
    auto outIStream = rmscrypto::api::CreateStreamFromStdStream(outStream);
    auto pStream    = ProtectedFileStream::Create(policy, outIStream, fileExt);

    // preparing
    readPosition  = 0;
    writePosition = pStream->Size();

    inStream->seekg(0, ios::end);
    totalSize = inStream->tellg();

    // start threads
    for (size_t i = 0; i < THREADS_NUM; ++i) {
      threadPool.push_back(thread(WorkerThread,
                                  static_pointer_cast<iostream>(inStream),
                                  pStream,
                                  true));
    }

    for (thread&amp; t: threadPool) {
      if (t.joinable()) {
        t.join();
      }
    }

    pStream->Flush();
  }
}
```



</dl> </dd> </dl>

## **Scenario**: Protect a file using custom protection

<dl> <dl> **Protects a file using custom protectionSource**: [rms\_sample/mainwindow.cpp](https://github.com/AzureAD/rms-sdk-for-cpp/tree/master/samples/rms_sample)  
**Description**: After getting a file name from the user, reading the certificates (see *MainWindow::addCertificates*), collecting rights information from the user, and setting up the authorization callback with Client ID and Redirect URL, the selected file is projected by calling *ConvertToPFilePredefinedRights* (see following code example).  


```C++
void MainWindow::ConvertToPFILEUsingRights(const string            & fileIn,
                                           const vector<UserRights>&amp; userRights,
                                           const string            & clientId,
                                           const string            & redirectUrl,
                                           const string            & clientEmail)
{
  // generate output filename
  string fileOut = fileIn + ".pfile";

  // add trusted certificates using HttpHelpers of RMS and Auth SDKs
  addCertificates();

  // create shared in/out streams
  auto inFile = make_shared<ifstream>(
    fileIn, ios_base::in | ios_base::binary);
  auto outFile = make_shared<fstream>(
    fileOut, ios_base::in | ios_base::out | ios_base::trunc | ios_base::binary);

  if (!inFile->is_open()) {
    AddLog("ERROR: Failed to open ", fileIn.c_str());
    return;
  }

  if (!outFile->is_open()) {
    AddLog("ERROR: Failed to open ", fileOut.c_str());
    return;
  }

  // find file extension
  string fileExt;
  auto   pos = fileIn.find_last_of('.');

  if (pos != string::npos) {
    fileExt = fileIn.substr(pos);
  }

  // is anything to add
  if (userRights.size() == 0) {
    AddLog("ERROR: ", "Please fill email and check rights");
    return;
  }


  try {
    // create authentication callback
    AuthCallback auth(clientId, redirectUrl);

    // process convertion
    PFileConverter::ConvertToPFilePredefinedRights(
      clientEmail,
      inFile,
      fileExt,
      outFile,
      auth,
      this->consent,
      userRights);

    AddLog("Successfully converted to ", fileOut.c_str());
  }
  catch (const rmsauth::Exception&amp; e) {
    AddLog("ERROR: ", e.error().c_str());

    outFile->close();
    remove(fileOut.c_str());
  }
  catch (const rmscore::exceptions::RMSException&amp; e) {
    AddLog("ERROR: ", e.what());

    outFile->close();
    remove(fileOut.c_str());
  }
  inFile->close();
  outFile->close();
}
```



**Creates a protection policy give user selected rightsSource**: [rms\_sample/pfileconverter.cpp](https://github.com/AzureAD/rms-sdk-for-cpp/tree/master/samples/rms_sample)  
**Description**: Create a policy descriptor and fill it with the user's rights information then, use the policy descriptor to create a user policy. This policy is used to protect the selected file via a call to *ConvertToPFileUsingPolicy* (see this described in a previous section of this topic).  


```C++
void PFileConverter::ConvertToPFilePredefinedRights(
  const string            & userId,
  shared_ptr<istream>       inStream,
  const string            & fileExt,
  shared_ptr<iostream>      outStream,
  IAuthenticationCallback & auth,
  IConsentCallback&amp; /*consent*/,
  const vector<UserRights>&amp; userRights)
{
  auto endValidation = chrono::system_clock::now() + chrono::hours(48);


  PolicyDescriptor desc(userRights);

  desc.Referrer(make_shared<string>("https://client.test.app"));
  desc.ContentValidUntil(endValidation);
  desc.AllowOfflineAccess(false);
  desc.Name("Test Name");
  desc.Description("Test Description");

  auto policy = UserPolicy::Create(desc, userId, auth,
                                   USER_AllowAuditedExtraction);
  ConvertToPFileUsingPolicy(policy, inStream, fileExt, outStream);
}
 
```



</dl> </dd> </dl>

## WorkerThread - a supporting method

<dl> The *WorkerThread()* method is called by two of the previous example scenarios; **Create a protected file stream** and **Protects a file given a policy** in the following manner:


```C++
threadPool.push_back(thread(WorkerThread,
                                  static_pointer_cast<iostream>(outStream), pfs,
                                  false));
```



  
**Supporting method, WorkerThread()**  


```C++
static mutex   threadLocker;
static int64_t totalSize     = 0;
static int64_t readPosition  = 0;
static int64_t writePosition = 0;
static vector<thread> threadPool;

static void WorkerThread(shared_ptr<iostream>           stdStream,
                         shared_ptr<ProtectedFileStream>pStream,
                         bool                           modeWrite) {
  vector<uint8_t> buffer(4096);
  int64_t bufferSize = static_cast<int64_t>(buffer.size());

  while (totalSize - readPosition > 0) {
    // lock
    threadLocker.lock();

    // check remain
    if (totalSize - readPosition <= 0) {
      threadLocker.unlock();
      return;
    }

    // get read/write offset
    int64_t offsetRead  = readPosition;
    int64_t offsetWrite = writePosition;
    int64_t toProcess   = min(bufferSize, totalSize - readPosition);
    readPosition  += toProcess;
    writePosition += toProcess;

    // no need to lock more
    threadLocker.unlock();

    if (modeWrite) {
      // stdStream is not thread safe!!!
      try {
        threadLocker.lock();

        stdStream->seekg(offsetRead);
        stdStream->read(reinterpret_cast<char *>(&amp;buffer[0]), toProcess);
        threadLocker.unlock();
        auto written =
          pStream->WriteAsync(
            buffer.data(), toProcess, offsetWrite, std::launch::deferred).get();

        if (written != toProcess) {
          throw rmscore::exceptions::RMSStreamException("Error while writing data");
        }
      }
      catch (exception&amp; e) {
        qDebug() << "Exception: " << e.what();
      }
    } else {
      auto read =
        pStream->ReadAsync(&amp;buffer[0],
                           toProcess,
                           offsetRead,
                           std::launch::deferred).get();

      if (read == 0) {
        break;
      }

      try {
        // stdStream is not thread safe!!!
        threadLocker.lock();

        // seek to write
        stdStream->seekp(offsetWrite);
        stdStream->write(reinterpret_cast<const char *>(buffer.data()), read);
        threadLocker.unlock();
      }
      catch (exception&amp; e) {
        qDebug() << "Exception: " << e.what();
      }
    }
  }
}
```



</dl>

## **Scenario**: RMS authentication

<dl> The following examples show two different authentication approaches; obtaining Azure Authentication oAuth2 token using UI and without UI.<dl> **Acquiring oAuth2 Authentication Token with UISource**: [rmsauth\_sample/mainwindow.cpp](https://github.com/AzureAD/rms-sdk-for-cpp/tree/master/samples/rmsauth_sample)  
<dl> **Step 1**: Create a shared point of **rmsauth::FileCache** object.Description: You can set cache path or use default.  


```C++
auto FileCachePtr = std::make_shared< rmsauth::FileCache>();
```



**Step 2**: Create **rmsauth::AuthenticationContext** objectDescription: Specify Azure *authority URI* and *FileCache* object.


```C++
AuthenticationContext authContext(
                              std::string(“https://sts.aadrm.com/_sts/oauth/authorize”),
                              AuthorityValidationType::False,
                              FileCachePtr);

```



  
**Step 3**: Call **aquireToken** method of **authContext** object and specify next parameters:Description:

-   *Requested resource* - protected resource you want to access
-   *Client unique ID* - usually a GUID
-   *Redirection URI* - the URI which will be readdressed after authentication token fetched
-   *Authentication prompt behavior* - if you set **PromptBehavior::Auto** the library tries to use cache and refresh token if necessary
-   *User ID* - User name displayed in the prompt window


```C++
auto result = authContext.acquireToken(
                std::string(“api.aadrm.com”),
                std::string(“4a63455a-cfa1-4ac6-bd2e-0d046cf1c3f7”),
                std::string(“https://client.test.app”),
                PromptBehavior::Auto,
                std::string(“john.smith@msopentechtest01.onmicrosoft.com”));

```



  
**Step 4**: Get access token from resultDescription: Call **result-&gt; accessToken()** method

> [!Note]  
> Any of the authentication library methods may raise **rmsauth::Exception**

 

  
</dl> </dd> **Acquiring oAuth2 Authentication Token without UISource**: [rmsauth\_sample/mainwindow.cpp](https://github.com/AzureAD/rms-sdk-for-cpp/tree/master/samples/rmsauth_sample)  
  
<dl> **Step 1**: Create a shared point of **rmsauth::FileCache** objectDescription: You can set cache path or use default  


```C++
auto FileCachePtr = std::make_shared< rmsauth::FileCache>();
```



**Step 2**:Create **UserCredential** objectDescription: Specify *user login* and *password*


```C++
auto userCred = std::make_shared<UserCredential>("john.smith@msopentechtest01.onmicrosoft.com",
                                                 "SomePass");
```



  
**Step 3**:Create **rmsauth::AuthenticationContext** objectDescription: Specify Azure authority *URI* and *FileCache* object


```C++
AuthenticationContext authContext(
                        std::string(“https://sts.aadrm.com/_sts/oauth/authorize”),
                        AuthorityValidationType::False,
                        FileCachePtr);
```



  
**Step 4**: Call the **aquireToken** method of **authContext** and specify parameters:

-   *Requested resource* - protected resource you want to access
-   *Client unique ID* - usually a GUID
-   *User credentials* - pass the created object


```C++
auto result = authContext.acquireToken(
                std::string(“api.aadrm.com”),
                std::string(“4a63455a-cfa1-4ac6-bd2e-0d046cf1c3f7”),
                userCred);
```



  
**Step 5**: Get access token from resultDescription: Call **result-&gt; accessToken()** method

> [!Note]  
> Any of the authentication library methods may raise **rmsauth::Exception**

 

  
</dl> </dd> </dl> </dd> </dl>

 

 




