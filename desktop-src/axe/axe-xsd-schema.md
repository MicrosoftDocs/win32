---
title: AXE XSD Schema
description: This is the AXE XSD schema.
ms.assetid: 7C887BA8-B8DE-4871-AC11-5E394D605E72
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AXE XSD Schema

This is the AXE XSD schema.


```XML
<?xml version="1.0" encoding="utf-8"?>  
  
  
<xs:schema  
  version="1.1"  
  targetNamespace="http://www.microsoft.com/axe/assessment/manifest"  
  elementFormDefault="qualified"  
  xmlns="http://www.microsoft.com/axe/assessment/manifest"  
  xmlns:xs="http://www.w3.org/2001/XMLSchema"  
>  
    
  
  <xs:element name="AxeAssessmentManifest" type="AxeAssessmentManifest"/>  
  <xs:element name="AxeJobManifest" type="AxeJobManifest"/>  
  <xs:element name="AssessmentResult" type="AssessmentResult"/>  
  <xs:element name="AxeJobResults" type="AxeJobResults"/>  
  
  
  <xs:complexType name="Version">  
    <xs:all>  
      <xs:element name="Major" type="xs:unsignedInt"/>  
      <xs:element name="Minor" type="xs:unsignedInt"/>  
      <xs:element name="Build" type="xs:unsignedInt"/>  
      <xs:element name="Revision" type="xs:unsignedInt"/>  
    </xs:all>  
  </xs:complexType>  
  
  <xs:simpleType name="Guid">  
    <xs:restriction base="xs:string">  
      <xs:pattern value="\{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\}"/>  
    </xs:restriction>  
  </xs:simpleType>    
    
  <xs:complexType name="VersionedId">  
    <xs:all>  
      <xs:element name="Guid" type="Guid"/>  
      <xs:element name="Version" type="Version"/>  
    </xs:all>  
  </xs:complexType>  
      
  <xs:complexType name="_locTag">  
    <xs:simpleContent>  
      <xs:extension base="xs:string">  
        <xs:attribute name="_loc" type="xs:string" use="required"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  
  <xs:complexType name="_locDefinition">  
    <xs:sequence>  
      <xs:element name="_locDefault" minOccurs="0">  
        <xs:complexType>  
          <xs:attribute name="_loc" type="xs:string" use="required"/>  
          <xs:attribute name="_locID" type="xs:string" use="required"/>  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="_locTag" type="_locTag" minOccurs="0" maxOccurs="unbounded"/>  
    </xs:sequence>  
  </xs:complexType>  
      
  <xs:complexType name="DescriptionBasic">  
    <xs:all>  
      <xs:element name="ProgrammaticName" type="xs:string" minOccurs="0"/>  
      <xs:element name="DisplayName" type="LocalizedString" minOccurs="0"/>  
    </xs:all>  
  </xs:complexType>  
  
  <xs:complexType name="Description">  
    <xs:all>  
      <xs:element name="ProgrammaticName" type="xs:string" minOccurs="0"/>  
      <xs:element name="DisplayName" type="LocalizedString" minOccurs="0"/>  
      <xs:element name="ToolTip" type="LocalizedString" minOccurs="0"/>  
      <xs:element name="Information" type="LocalizedString" minOccurs="0"/>  
      <xs:element name="Tags" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element  
              name="Tag"  
              minOccurs="0"  
              maxOccurs="unbounded"  
              type="LocalizedString"/>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="Categories" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element  
              name="Category"  
              minOccurs="0"  
              maxOccurs="unbounded"  
              type="LocalizedString"/>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
    </xs:all>  
  </xs:complexType>  
  
  <xs:complexType name="LocalizedString">  
    <xs:simpleContent>  
      <xs:extension base="xs:string">  
        <xs:attribute name="_locID" type="xs:string" use="optional"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  
  <xs:complexType name="Empty">  
    <xs:complexContent>  
      <xs:restriction base="xs:anyType"/>  
    </xs:complexContent>  
  </xs:complexType>  
  
  <xs:complexType name="ErrorsAndWarnings">  
    <xs:choice maxOccurs="unbounded" minOccurs="0">  
      <xs:element name="Error" type="Error"/>  
      <xs:element name="Warning" type="Error"/>  
    </xs:choice>  
  </xs:complexType>  
  
  <xs:complexType name="NestedVerificationScope">  
    <xs:sequence>  
      <xs:any minOccurs="0" maxOccurs="unbounded" namespace="##any" processContents="skip"/>  
    </xs:sequence>  
    <xs:attribute name="SchemaVersion" type="xs:decimal" use="required" fixed="1.1"/>  
  </xs:complexType>    
  
  <xs:complexType name="StandardType">  
    <xs:choice>  
      <xs:element name="String" type="Empty"/>  
      <xs:element name="Int16" type="Empty"/>  
      <xs:element name="Int32" type="Empty"/>  
      <xs:element name="Int64" type="Empty"/>  
      <xs:element name="UInt16" type="Empty"/>  
      <xs:element name="UInt32" type="Empty"/>  
      <xs:element name="UInt64" type="Empty"/>  
      <xs:element name="Byte" type="Empty"/>  
      <xs:element name="SByte" type="Empty"/>  
      <xs:element name="Single" type="Empty"/>  
      <xs:element name="Double" type="Empty"/>  
      <xs:element name="Boolean" type="Empty"/>  
      <xs:element name="Char" type="Empty"/>  
      <xs:element name="DateTime" type="Empty"/>  
      <xs:element name="Duration" type="Empty"/>  
      <xs:element name="TimeSpan" type="Empty"/>  
      <xs:element name="FilePath" type="Empty"/>  
      <xs:element name="DirectoryPath" type="Empty"/>  
    </xs:choice>  
  </xs:complexType>  
  
  <xs:complexType name="JobKind">  
    <xs:choice>  
      <xs:element name="Normal" type="Empty"/>  
      <xs:element name="BatteryLife" type="Empty"/>  
      <xs:element name="DiagnosticModule" type="Empty"/>  
    </xs:choice>  
  </xs:complexType>  
  
  <xs:complexType name="SolutionData">  
    <xs:sequence>  
      <xs:any minOccurs="0" maxOccurs="unbounded" processContents="skip"/>  
    </xs:sequence>  
  </xs:complexType>  
  
  <xs:complexType name="LocalizedStringDictionaryEntry">  
    <xs:simpleContent>  
      <xs:extension base="xs:string">  
        <xs:attribute name="Id" type="xs:string" use="required"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
    
  <xs:element name="s" type="LocalizedStringDictionaryEntry"/>  
  
  <xs:complexType name="LocalizedStringDictionaryLanguage">  
    <xs:sequence>  
      <xs:element name="s" type="LocalizedStringDictionaryEntry" minOccurs="0" maxOccurs="unbounded"/>  
    </xs:sequence>  
  </xs:complexType>  
  
  <xs:element name="en" type="LocalizedStringDictionaryLanguage">  
    <xs:unique name="enStringDictionaryUniqueIds">  
      <xs:selector xpath="s"/>  
      <xs:field xpath="@Id"/>  
    </xs:unique>  
  </xs:element>  
  
  <xs:complexType name="LocalizedStringDictionary">  
    <xs:sequence>  
      <xs:any minOccurs="0" maxOccurs="unbounded" processContents="lax" namespace="##targetNamespace"/>  
    </xs:sequence>  
  </xs:complexType>  
    
  <xs:complexType name="Execution">  
    <xs:choice>  
      <xs:element name="CreateProcess">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="ApplicationName" type="xs:string"/>  
            <xs:element name="CreateNewConsole" type="Empty" minOccurs="0"/>  
            <xs:element name="CreateNoWindow" type="Empty" minOccurs="0"/>  
            <xs:element name="DetachedProcess" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresUIAccess" type="Empty" minOccurs="0"/>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="ShellExecute">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="ShellExecuteFile" type="xs:string"/>  
            <xs:element name="ShellExecuteVerb" type="xs:string"/>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
    </xs:choice>  
  </xs:complexType>  
  
    
  <xs:complexType name="ParameterDefinition">  
    <xs:all>  
      <xs:element name="Description" type="Description"/>  
  
      <xs:element name="Type" type="StandardType"/>  
  
      <xs:element name="DefaultValue" type="xs:string" minOccurs="0"/>  
      <xs:element name="BenchmarkValue" type="xs:string" minOccurs="0"/>  
  
      <xs:element name="Constraints" minOccurs="0">  
        <xs:complexType>  
          <xs:choice>  
            <xs:element name="LengthConstraint" type="xs:unsignedInt"/>  
            <xs:sequence>  
              <xs:element name="MinimumConstraint" type="xs:string" minOccurs="0"/>  
              <xs:element name="MaximumConstraint" type="xs:string" minOccurs="0"/>  
            </xs:sequence>  
          </xs:choice>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="CommandLineFormat" type="xs:string" minOccurs="0"/>  
      <xs:element name="Ordinal" type="xs:unsignedInt" minOccurs="0"/>  
  
      <xs:element name="Visibility" minOccurs="0">  
        <xs:complexType>  
          <xs:choice>  
            <xs:element name="Visible" type="Empty"/>  
            <xs:element name="Hidden" type="Empty"/>  
            <xs:element name="Collapsed" type="Empty"/>  
          </xs:choice>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="Inclusion" minOccurs="0">  
        <xs:complexType>  
          <xs:choice>  
            <xs:element name="Optional" type="Empty"/>  
            <xs:element name="OptionalIncluded" type="Empty"/>  
            <xs:element name="Required" type="Empty"/>  
          </xs:choice>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="PresentWith" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="ParameterIds">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="ParameterId" maxOccurs="unbounded">  
                    <xs:complexType>  
                      <xs:all>  
                        <xs:element name="ProgrammaticName" type="xs:string"/>  
                        <xs:element name="Value" type="xs:string" minOccurs="0"/>  
                      </xs:all>  
                    </xs:complexType>  
                  </xs:element>  
                </xs:sequence>  
              </xs:complexType>  
              <xs:unique name="ParameterDefinitionPresentWithParameterIdsUniqueProgrammaticNames">  
                <xs:selector xpath="ParameterId"/>  
                <xs:field xpath="ProgrammaticName"/>  
              </xs:unique>  
            </xs:element>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
  
        
      <xs:element name="Flags" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="Flag" maxOccurs="unbounded">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="Description" type="Description"/>  
                  <xs:element name="Value" type="xs:string"/>  
                </xs:all>  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="Enumerations" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="Enumeration" maxOccurs="unbounded">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="Description" type="Description"/>  
                  <xs:element name="Value" type="xs:string"/>  
                </xs:all>  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
        
    </xs:all>  
  
  </xs:complexType>    
    
  <xs:complexType name="DiagnosticModule">  
    <xs:all>  
      <xs:element name="Id" type="Guid"/>  
      <xs:element name="CommandLineFormat" type="xs:string"/>  
      <xs:element name="Default" type="Empty" minOccurs="0"/>  
      <xs:element name="Required" type="Empty" minOccurs="0"/>  
    </xs:all>  
  </xs:complexType>  
    
  <xs:complexType name="TracingProfile">  
    <xs:all>  
      <xs:element name="ProgrammaticName" type="xs:string"/>  
      <xs:element name="FileName" type="xs:string"/>  
      <xs:element name="ProfileName" type="xs:string"/>  
      <xs:element name="MergeProfile" type="xs:string"/>  
    </xs:all>  
  </xs:complexType>  
    
  
  <xs:complexType name="MetricDefinition">  
    <xs:all>  
      <xs:element name="Description" type="Description"/>  
        
      <xs:element name="Type" type="StandardType"/>  
  
      <xs:element name="Units" type="xs:string" minOccurs="0"/>  
      <xs:element name="DecimalPlaces" type="xs:unsignedInt" minOccurs="0"/>  
      <xs:element name="Ordinal" type="xs:unsignedInt" minOccurs="0"/>  
  
      <xs:element name="BetterDirection" minOccurs="0">  
        <xs:complexType>  
          <xs:choice>  
            <xs:element name="None" type="Empty"/>  
            <xs:element name="Lower" type="Empty"/>  
            <xs:element name="Higher" type="Empty"/>  
          </xs:choice>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="PrimaryStatistic" minOccurs="0">  
        <xs:complexType>  
          <xs:choice>  
            <xs:element name="None" type="Empty"/>  
            <xs:element name="Mean" type="Empty"/>  
            <xs:element name="Median" type="Empty"/>  
          </xs:choice>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="SecondaryStatistic" minOccurs="0">  
        <xs:complexType>  
          <xs:choice>  
            <xs:element name="None" type="Empty"/>  
            <xs:element name="Mean" type="Empty"/>  
            <xs:element name="Median" type="Empty"/>  
          </xs:choice>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="Importance" type="xs:unsignedInt" minOccurs="0"/>  
        
    </xs:all>  
  
  </xs:complexType>  
    
  
  <xs:complexType name="MetricThresholdValue">  
    <xs:all>  
      <xs:element name="Description" type="Description"/>  
  
      <xs:element name="ValueType" type="StandardType"/>  
  
      <xs:element name="Value" type="xs:string"/>  
      
      <xs:element name="Comparison" minOccurs="0">  
        <xs:complexType>  
          <xs:choice>  
            <xs:element name="Absolute" type="Empty"/>  
            <xs:element name="Offset" type="Empty"/>  
            <xs:element name="Percent" type="Empty"/>  
            <xs:element name="TrueIsPass" type="Empty"/>  
            <xs:element name="FalseIsPass" type="Empty"/>  
            <xs:element name="ContainsStringIsPass" type="Empty"/>  
            <xs:element name="ContainsStringIsFail" type="Empty"/>  
            <xs:element name="IsStringIsPass" type="Empty"/>  
            <xs:element name="IsStringIsFail" type="Empty"/>  
            <xs:element name="RegularExpressionMatchIsPass" type="Empty"/>  
            <xs:element name="RegularExpressionMatchIsFail" type="Empty"/>  
          </xs:choice>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="Inclusion" minOccurs="0">  
        <xs:complexType>  
          <xs:choice>  
            <xs:element name="Inclusive" type="Empty"/>  
            <xs:element name="Exclusive" type="Empty"/>  
          </xs:choice>  
        </xs:complexType>  
      </xs:element>  
  
    </xs:all>  
  
  </xs:complexType>  
    
  
  <xs:complexType name="MetricThresholds">  
    <xs:sequence>  
      <xs:element name="MetricThreshold" maxOccurs="unbounded">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="Description" type="Description"/>  
            <xs:element name="MetricDefinitionProgrammaticName" type="xs:string"/>  
            <xs:element name="Target" type="xs:string" minOccurs="0"/>  
            <xs:element name="TestCaseKey" type="xs:string" minOccurs="0"/>  
            <xs:element name="Ordinal" type="xs:unsignedInt" minOccurs="0"/>  
            <xs:element name="MetricThresholdValues" minOccurs="0">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="MetricThresholdValue" type="MetricThresholdValue" minOccurs="1" maxOccurs="2"/>  
                </xs:sequence>  
              </xs:complexType>  
            </xs:element>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
  </xs:complexType>  
  
  <xs:complexType name="Columns">  
    <xs:sequence>  
      <xs:element name="Column" minOccurs="0" maxOccurs="unbounded">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="Metric" type="xs:string"/>  
            <xs:element name="TestCaseKey" type="xs:string" minOccurs="0"/>  
            <xs:element name="TestCaseName" type="LocalizedString" minOccurs="0"/>  
            <xs:element name="TestCaseToolTip" type="LocalizedString" minOccurs="0"/>  
            <xs:element name="Charted" type="xs:string" minOccurs="0"/>  
            <xs:element name="Hidden" type="xs:string" minOccurs="0"/>  
            <xs:element name="PageLink" type="xs:string" minOccurs="0"/>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
  </xs:complexType>    
  
  
  <xs:complexType name="AxeAssessmentManifest">  
    <xs:all>  
  
      <xs:element name="Ordinal" type="xs:unsignedInt" minOccurs="0"/>  
  
      <xs:element name="_locDefinition" type="_locDefinition" minOccurs="0"/>  
        
      <xs:element name="VersionedId" type="VersionedId"/>  
  
      <xs:element name="MinimumAxeVersionRequired">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="Version" type="Version"/>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="Description" type="Description"/>  
  
      <xs:element name="Properties" minOccurs="0">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="FilePath" type="xs:string" minOccurs="0"/>  
            <xs:element name="Author" type="LocalizedString" minOccurs="0"/>  
            <xs:element name="IconResource" type="xs:string" minOccurs="0"/>  
            <xs:element name="Copyright" type="LocalizedString" minOccurs="0"/>  
            <xs:element name="Url" type="xs:anyURI" minOccurs="0"/>  
            <xs:element name="UpdateUrl" type="xs:anyURI" minOccurs="0"/>  
            <xs:element name="AuthorUrl" type="xs:anyURI" minOccurs="0"/>  
            <xs:element name="LastSavedTimeAndDate" type="xs:dateTime" minOccurs="0"/>  
            <xs:element name="OnlyForProcessor" minOccurs="0">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="X86" type="Empty" minOccurs="0"/>  
                  <xs:element name="X64" type="Empty" minOccurs="0"/>  
                  <xs:element name="ARM" type="Empty" minOccurs="0"/>  
                </xs:all>  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="SupportsWindowsPE" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresACPower" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresACPowerWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="BasicDisplayWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="BasicDisplayBlock" type="Empty" minOccurs="0"/>  
            <xs:element name="NoInteractionInfo" type="Empty" minOccurs="0"/>  
            <xs:element name="MayEmptyRecycleBinInfo" type="Empty" minOccurs="0"/>  
            <xs:element name="LockOnWakeBlock" type="Empty" minOccurs="0"/>  
            <xs:element name="HibernateDisabledBlock" type="Empty" minOccurs="0"/>  
            <xs:element name="ConnectedStandbyDisabledBlock" type="Empty" minOccurs="0"/>  
            <xs:element name="WirelessDisconnectedWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="AVOffWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="PowerProfileNotBalancedWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresAutoLogOnWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresAutoLogOnBlock" type="Empty" minOccurs="0"/>  
            <xs:element name="KernelDebuggerWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="DriverVerifierWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="SystemDiskLegacyModeWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="ProblemDevicesWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresBattery" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresTracing" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresTracingWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="SupportsRunningRemote" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresDisplay" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresExecution" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresNoExecution" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresInternet" type="Empty" minOccurs="0"/>  
            <xs:element name="MayRebootSystem" type="Empty" minOccurs="0"/>  
            <xs:element name="ShouldRunSilent" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresElevation" type="Empty" minOccurs="0"/>  
            <xs:element name="ScreensaverPasswordWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresAudioRenderDeviceWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="RequiresWindowsGenuineWarn" type="Empty" minOccurs="0"/>  
            <xs:element name="EstimatedRunTime" type="xs:unsignedLong" minOccurs="0"/>  
            <xs:element name="WatchDogTimeOut" type="xs:unsignedLong" minOccurs="0"/>  
            <xs:element name="VersionNote" type="LocalizedString" minOccurs="0"/>  
            <xs:element name="JobKind" type="JobKind" minOccurs="0"/>  
            <xs:element name="ExitValueMeaning" minOccurs="0">  
              <xs:complexType>  
                <xs:choice>  
                  <xs:element name="ZeroIsSuccess" type="Empty"/>  
                  <xs:element name="ExitValueIsHresult" type="Empty"/>  
                </xs:choice>  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="ProcessIdleTasks" minOccurs="0">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="HoursSinceLastRun" type="xs:positiveInteger" />  
                </xs:all>  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="VerifyOSVersion" minOccurs="0">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="Version" type="Version"/>  
                </xs:all>  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="CheckForProcess" minOccurs="0">  
              <xs:complexType>  
                <xs:choice minOccurs="1" maxOccurs="unbounded">  
                  <xs:element name="Block" type="xs:string"/>  
                  <xs:element name="Warn" type="xs:string"/>  
                </xs:choice>  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="RequiresAppVersions" minOccurs="0">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="AppVersion" maxOccurs="unbounded">  
                    <xs:complexType>  
                      <xs:all>  
                        <xs:element name="App" type="xs:string"/>  
                        <xs:element name="Version" type="Version"/>  
                      </xs:all>  
                    </xs:complexType>  
                  </xs:element>  
                </xs:sequence>  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="EventTracing" minOccurs="0">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="BufferSize" type="xs:unsignedInt" minOccurs="0"/>  
                  <xs:element name="MinimumBuffers" type="xs:unsignedInt" minOccurs="0"/>  
                  <xs:element name="MaximumBuffers" type="xs:unsignedInt" minOccurs="0"/>  
                  <xs:element name="LoggingMode" minOccurs="0">  
                    <xs:complexType>  
                      <xs:choice>  
                        <xs:element name="NoPerProcessorBuffering" type="Empty"/>  
                      </xs:choice>  
                    </xs:complexType>  
                  </xs:element>  
                </xs:all>  
              </xs:complexType>  
            </xs:element>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="Diagnostics" minOccurs="0">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="DiagnosticModules" minOccurs="0">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="DiagnosticModule" type="DiagnosticModule" maxOccurs="unbounded"/>  
                </xs:sequence>  
              </xs:complexType>  
              <xs:unique name="AxeAssessmentManifestDiagnosticModulesUniqueIds">  
                <xs:selector xpath="DiagnosticModule"/>  
                <xs:field xpath="Id"/>  
              </xs:unique>  
            </xs:element>  
            <xs:element name="TracingProfiles" minOccurs="0">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="TracingProfile" type="TracingProfile" maxOccurs="unbounded"/>  
                </xs:sequence>  
              </xs:complexType>  
              <xs:unique name="AxeAssessmentManifestTracingProfilesUniqueProgrammaticNames">  
                <xs:selector xpath="TracingProfile"/>  
                <xs:field xpath="ProgrammaticName"/>  
              </xs:unique>  
            </xs:element>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="ParameterDefinitions" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="ParameterDefinition" type="ParameterDefinition" maxOccurs="unbounded"/>  
          </xs:sequence>  
        </xs:complexType>  
        <xs:unique name="AxeAssessmentManifestParameterDefinitionsUniqueProgrammaticNames">  
          <xs:selector xpath="ParameterDefinition"/>  
          <xs:field xpath="Description/ProgrammaticName"/>  
        </xs:unique>  
      </xs:element>  
  
      <xs:element name="MetricDefinitions" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="MetricDefinition" type="MetricDefinition" maxOccurs="unbounded"/>  
          </xs:sequence>  
        </xs:complexType>  
        <xs:unique name="AxeAssessmentManifestMetricDefinitionsUniqueProgrammaticNames">  
          <xs:selector xpath="MetricDefinition"/>  
          <xs:field xpath="Description/ProgrammaticName"/>  
        </xs:unique>  
      </xs:element>  
  
      <xs:element name="MetricThresholds" type="MetricThresholds" minOccurs="0"/>  
  
      <xs:element name="Execution" type="Execution" minOccurs="0"/>  
  
      <xs:element name="Commands" minOccurs="0">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="ExecuteWorkload" type="Execution" minOccurs="0"/>  
            <xs:element name="AnalyzeFolder" type="Execution" minOccurs="0"/>  
            <xs:element name="AnalyzeTrace" type="Execution" minOccurs="0"/>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="SolutionData" type="SolutionData" minOccurs="0"/>  
  
      <xs:element name="LocalizedStringDictionary" type="LocalizedStringDictionary" minOccurs="0"/>  
  
      <xs:element name="PresentationHints" minOccurs="0">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="Columns" type="Columns"/>  
            <xs:element name="PageLink" type="xs:string" minOccurs="0"/>  
            <xs:element name="Pages" minOccurs="0">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="Page" minOccurs="0" maxOccurs="unbounded">  
                    <xs:complexType>  
                      <xs:all>  
                        <xs:element name="Description" type="Description"/>  
                        <xs:element name="Groups" minOccurs="0">  
                          <xs:complexType>  
                            <xs:sequence>  
                              <xs:element name="Group" minOccurs="0" maxOccurs="unbounded">  
                                <xs:complexType>  
                                  <xs:all>  
                                    <xs:element name="Description" minOccurs="0">  
                                      <xs:complexType>  
                                        <xs:all>  
                                          <xs:element name="DisplayName" type="LocalizedString" minOccurs="0"/>  
                                          <xs:element name="ToolTip" type="LocalizedString" minOccurs="0"/>  
                                        </xs:all>  
                                      </xs:complexType>  
                                    </xs:element>  
                                    <xs:element name="Columns" type="Columns"/>  
                                    <xs:element name="PageLink" type="xs:string" minOccurs="0"/>  
                                  </xs:all>  
                                </xs:complexType>  
                              </xs:element>  
                            </xs:sequence>  
                          </xs:complexType>  
                        </xs:element>  
                        <xs:element name="TestCaseTable" minOccurs="0">  
                          <xs:complexType>  
                            <xs:all>  
                              <xs:element name="Description" minOccurs="0">  
                                <xs:complexType>  
                                  <xs:all>  
                                    <xs:element name="DisplayName" type="LocalizedString" minOccurs="0"/>  
                                    <xs:element name="ToolTip" type="LocalizedString" minOccurs="0"/>  
                                  </xs:all>  
                                </xs:complexType>  
                              </xs:element>  
                              <xs:element name="Columns" type="Columns"/>  
                              <xs:element name="PageLink" type="xs:string" minOccurs="0"/>  
                              <xs:element name="TestCaseKey" type="xs:string" minOccurs="0"/>  
                              <xs:element name="Sort" type="xs:string" minOccurs="0"/>  
                              <xs:element name="SortAscending" type="xs:string" minOccurs="0"/>  
                              <xs:element name="GroupBy" type="xs:string" minOccurs="0"/>  
                              <xs:element name="Filter" minOccurs="0">  
                                <xs:complexType>  
                                  <xs:sequence>  
                                    <xs:any processContents="skip"/>  
                                  </xs:sequence>  
                                </xs:complexType>  
                              </xs:element>  
                            </xs:all>  
                          </xs:complexType>  
                        </xs:element>  
                      </xs:all>  
                    </xs:complexType>  
                  </xs:element>  
                </xs:sequence>  
              </xs:complexType>  
            </xs:element>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>   
    </xs:all>  
    <xs:attribute name="SchemaVersion" type="xs:decimal" use="required" fixed="1.1"/>  
  </xs:complexType>  
  
  
  <xs:complexType name="AssessmentRun">  
    <xs:all>  
      <xs:element name="Id" type="Guid"/>  
      <xs:element name="AssessmentId" type="VersionedId"/>  
      <xs:element name="Name" type="xs:string" minOccurs="0"/>  
      <xs:element name="DisplayName" type="xs:string" minOccurs="0"/>  
      <xs:element name="SolutionData" type="SolutionData" minOccurs="0"/>  
        
      <xs:element name="CommandLine" type="xs:string" minOccurs="0"/>  
        
      <xs:element name="BenchmarkMode" type="xs:string" minOccurs="0"/>  
      <xs:element name="Ordinal" type="xs:string" minOccurs="0"/>  
  
      <xs:element name="ParameterValues" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="ParameterValue" maxOccurs="unbounded">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="ProgrammaticName" type="xs:string"/>  
                  <xs:element name="Value" type="xs:string"/>  
                </xs:all>  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="DiagnosticModules" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="DiagnosticModuleId" maxOccurs="unbounded">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="Guid" type="Guid"/>  
                  <xs:element name="Version" type="Version"/>  
                </xs:all>  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="AssessmentRuns" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="AssessmentRun" type="AssessmentRun" maxOccurs="unbounded"/>  
          </xs:sequence>  
        </xs:complexType>  
        <xs:unique name="AssessmentRunsAssessmentRunsUniqueId">  
          <xs:selector xpath="AssessmentRun"/>  
          <xs:field xpath="Id"/>  
        </xs:unique>  
      </xs:element>  
        
    </xs:all>  
      
  </xs:complexType>  
  
  <xs:complexType name="JobParameters">  
    <xs:all>  
      <xs:element name="Image" type="xs:string" minOccurs="0"/>  
      <xs:element name="EarliestStartTime" type="xs:dateTime" minOccurs="0"/>  
      <xs:element name="KeepTempFiles" type="Empty" minOccurs="0"/>  
      <xs:element name="CollectOnly" type="Empty" minOccurs="0"/>  
      <xs:element name="ResultsPublishPath" type="xs:string" minOccurs="0"/>  
      <xs:element name="UserString" type="xs:string" minOccurs="0"/>  
      <xs:element name="StopOnAssessmentError" type="Empty" minOccurs="0"/>  
      <xs:element name="RunSilently" type="Empty" minOccurs="0"/>  
      <xs:element name="SkipMachineConfiguration" type="Empty" minOccurs="0"/>  
      <xs:element name="SolutionUX" minOccurs="0">  
        <xs:complexType>  
          <xs:choice>  
            <xs:element name="Normal" type="Empty"/>  
            <xs:element name="Console" type="Empty"/>  
            <xs:element name="Silent" type="Empty"/>  
          </xs:choice>  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="JobKind" type="JobKind" minOccurs="0"/>  
      <xs:element name="AssessmentContentRoot" type="xs:string" minOccurs="0"/>  
      <xs:element name="PostExecutionAction" type="Execution" minOccurs="0"/>  
      <xs:element name="BenchmarkMode" type="Empty" minOccurs="0"/>  
    </xs:all>  
  </xs:complexType>  
  
  <xs:complexType name="AxeJobManifest">  
    <xs:all>  
      <xs:element name="VersionedId" type="VersionedId"/>  
  
      <xs:element name="MinimumAxeVersionRequired">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="Version" type="Version"/>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="Description" type="Description"/>  
  
      <xs:element name="JobParameters" type="JobParameters" minOccurs="0"/>  
        
      <xs:element name="Properties" minOccurs="0">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="LastSavedId" type="Guid" minOccurs="0"/>  
            <xs:element name="LastSavedTimeAndDate" type="xs:dateTime" minOccurs="0"/>  
            <xs:element name="VersionNote" type="xs:string" minOccurs="0"/>  
            <xs:element name="IsTemplate" type="xs:string" minOccurs="0"/>  
            <xs:element name="IconResource" type="xs:string" minOccurs="0"/>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="AssessmentManifests" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="AxeAssessmentManifest" type="NestedVerificationScope" maxOccurs="unbounded"/>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="AssessmentRuns" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="AssessmentRun" type="AssessmentRun" maxOccurs="unbounded"/>  
          </xs:sequence>  
        </xs:complexType>  
        <xs:unique name="AxeJobManifestAssessmentRunsUniqueId">  
          <xs:selector xpath="AssessmentRun"/>  
          <xs:field xpath="Id"/>  
        </xs:unique>  
      </xs:element>  
  
      <xs:element name="SolutionData" type="SolutionData" minOccurs="0"/>  
  
      <xs:element name="LocalizedStringDictionary" type="LocalizedStringDictionary" minOccurs="0"/>  
        
    </xs:all>  
    <xs:attribute name="SchemaVersion" type="xs:decimal" use="required" fixed="1.1"/>  
  </xs:complexType>  
  
  
  <xs:complexType name="Error">  
    <xs:all>  
      <xs:element name="Message" type="xs:string"/>  
      <xs:element name="Hresult" type="xs:string" minOccurs="0"/>  
    </xs:all>  
  </xs:complexType>  
  
  <xs:complexType name="MetricValues">  
    <xs:sequence>  
      <xs:element name="MetricValue" maxOccurs="unbounded">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="ProgrammaticName" type="xs:string"/>  
            <xs:element name="Value" type="xs:string"/>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
  </xs:complexType>  
  
  <xs:complexType name="Links">  
    <xs:sequence>  
      <xs:element name="Link" maxOccurs="unbounded">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="LinkTitle" type="xs:string"/>  
            <xs:element name="LinkToolTip" type="xs:string" minOccurs="0"/>  
            <xs:element name="LinkURI" type="xs:string"/>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
  </xs:complexType>  
  
  <xs:complexType name="Issues">  
    <xs:sequence>  
      <xs:element name="Issue" maxOccurs="unbounded">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="IssueTitle" type="xs:string" minOccurs="0"/>  
            <xs:element name="IssueDescription" type="xs:string" minOccurs="0"/>  
            <xs:element name="IssueToolTip" type="xs:string" minOccurs="0"/>  
  
            <xs:element name="Class" type="Description" minOccurs="0"/>  
              
            <xs:element name="Solution" minOccurs="0">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="Description" type="xs:string" minOccurs="0"/>  
                  <xs:element name="Links" type="Links" minOccurs="0"/>  
                </xs:all>  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="AnalysisLinks" type="Links" minOccurs="0"/>  
            <xs:element name="AffectedMetrics" minOccurs="0">  
              <xs:complexType >  
                <xs:sequence>  
                  <xs:element name="MetricReference" type="xs:string" maxOccurs="unbounded"/>  
                </xs:sequence>  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="Categories" minOccurs="0">  
              <xs:complexType >  
                <xs:sequence>  
                  <xs:element name="Category" type="xs:string" maxOccurs="unbounded"/>  
                </xs:sequence>  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="EqualityId" type="xs:string" minOccurs="0"/>  
            <xs:element name="TypeID" type="xs:string" minOccurs="0"/>  
            <xs:element name="Impact" minOccurs="0">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="RelatedActivities" minOccurs="0">  
                    <xs:complexType>  
                      <xs:sequence>  
                        <xs:element name="ActivityReference" maxOccurs="unbounded">  
                          <xs:complexType>  
                            <xs:attribute name="ActivityID" type="xs:string" use="required"/>  
                          </xs:complexType>  
                        </xs:element>  
                      </xs:sequence>  
                    </xs:complexType>  
                  </xs:element>  
                  <xs:element name="SolutionData" type="SolutionData" minOccurs="0"/>  
                </xs:all>  
                <xs:attribute name="Severity" type="xs:unsignedInt" use="optional"/>  
              </xs:complexType>  
            </xs:element>  
              
            <xs:element name="SolutionData" type="SolutionData" minOccurs="0"/>  
            <xs:element name="MetricValues" type="MetricValues" minOccurs="0"/>  
          </xs:all>  
  
          <xs:attribute name="TestCase" type="xs:string" use="optional"/>  
  
          <xs:attribute name="Known" type="xs:string" use="optional"/>  
          <xs:attribute name="ID" type="xs:string" use="optional"/>  
  
          <xs:attribute name="Summary" type="xs:string" use="optional"/>  
  
          <xs:attribute name="parentID" type="xs:string" use="optional"/>  
            
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
  </xs:complexType>  
  
  <xs:complexType name="Trace">  
    <xs:all minOccurs="0">  
      <xs:element name="Description" minOccurs="0">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="Name" type="xs:string"/>  
            <xs:element name="ToolTip" type="xs:string" minOccurs="0"/>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="File">  
        <xs:simpleType>  
          <xs:restriction base="xs:string">  
            <xs:minLength value="1"/>  
          </xs:restriction>  
        </xs:simpleType>  
      </xs:element>  
      <xs:element name="Link" type="xs:string" minOccurs="0"/>  
      <xs:element name="TraceProfiles" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="TraceProfile" type="TraceProfileUsed" maxOccurs="unbounded"/>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
    </xs:all>  
  </xs:complexType>  
  
  <xs:complexType name="TraceProfileUsed">  
    <xs:all>  
      <xs:element name="ProgrammaticName" type="xs:string"/>  
      <xs:element name="Guid" type="Guid"/>  
    </xs:all>  
  </xs:complexType>  
  
  <xs:complexType name="AxeRunInfo">  
    <xs:all>  
      <xs:element name="Error" type="xs:int"/>  
      <xs:element name="ExitCode" type="xs:int" minOccurs="0"/>  
      <xs:element name="ResultsLocation" type="xs:string"/>  
      <xs:element name="Start" type="xs:dateTime"/>  
      <xs:element name="Duration" type="xs:unsignedLong"/>  
      <xs:element name="Reboots" type="xs:unsignedLong"/>  
      <xs:element name="CannotAnalyzeReason" minOccurs="0">  
        <xs:complexType>  
          <xs:choice>  
            <xs:element name="NotSupported" type="Empty"/>  
            <xs:element name="ExecutionFailed" type="Empty"/>  
          </xs:choice>  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="ErrorsAndWarnings" type="ErrorsAndWarnings" minOccurs="0" />  
      <xs:element name="LogFiles" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="LogFile" type="xs:string" maxOccurs="unbounded"/>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
    </xs:all>  
  </xs:complexType>  
  
  <xs:complexType name="AssessmentResult">  
    <xs:all>  
      <xs:element name="Guid" type="Guid"/>  
      <xs:element name="ManifestId" type="VersionedId"/>  
      <xs:element name="ExecutionInfo" type="AxeRunInfo"/>  
      <xs:element name="AnalysisInfo" type="AxeRunInfo" minOccurs="0"/>  
      <xs:element name="ExitCode" type="xs:int" minOccurs="0"/>  
      <xs:element name="ResultsLocation" type="xs:string" minOccurs="0"/>  
      <xs:element name="ErrorsAndWarnings" type="ErrorsAndWarnings" minOccurs="0" />  
      <xs:element name="LogFiles" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="LogFile" type="xs:string" maxOccurs="unbounded"/>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="Iterations" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="Iteration" maxOccurs="unbounded">  
              <xs:complexType>  
                <xs:all>  
                    
                  <xs:element name="Description" type="Description" minOccurs="0"/>  
                    
                  <xs:element name="Activities" minOccurs="0">  
                    <xs:complexType>  
                      <xs:sequence>  
                        <xs:element name="Activity" minOccurs="0" maxOccurs="unbounded">  
                          <xs:complexType>  
                            <xs:all>  
                                
                              <xs:element name="ActivityInstance" type="xs:string" minOccurs="0"/>  
                                
                              <xs:element name="ActivityInstanceDisplayName" type="LocalizedString" minOccurs="0"/>  
  
                              <xs:element name="ActivityClassDisplayName" type="LocalizedString" minOccurs="0"/>  
  
                              <xs:element name="Importance" type="xs:unsignedInt" minOccurs="0"/>  
  
                              <xs:element name="Trace" type="Trace" minOccurs="0"/>  
                                
                              <xs:element name="ActivityTitle" type="xs:string" minOccurs="0"/>  
                              <xs:element name="ActivityDescription" type="xs:string" minOccurs="0"/>  
                              <xs:element name="ActivityClass" type="xs:string" minOccurs="0"/>  
                              <xs:element name="ActivityStartTime" type="xs:double" minOccurs="0"/>  
                              <xs:element name="ActivityEndTime" type="xs:double" minOccurs="0"/>  
                              <xs:element name="ActivityStartThread" type="xs:int" minOccurs="0"/>  
                              <xs:element name="ActivityEndThread" type="xs:int" minOccurs="0"/>  
                              <xs:element name="References" minOccurs="0">  
                                <xs:complexType>  
                                  <xs:sequence>  
                                    <xs:element name="IssueReference" maxOccurs="unbounded">  
                                      <xs:complexType>  
                                        <xs:attribute name="IssueID" type="xs:string" use="required"/>  
                                      </xs:complexType>  
                                    </xs:element>  
                                  </xs:sequence>  
                                </xs:complexType>  
                              </xs:element>  
                            </xs:all>  
                            <xs:attribute name="ID" type="xs:string" use="optional"/>  
                            <xs:attribute name="parentID" type="xs:string" use="optional"/>  
                          </xs:complexType>  
                        </xs:element>  
                      </xs:sequence>  
                    </xs:complexType>  
                  </xs:element>  
                  <xs:element name="MetricValues" type="MetricValues" minOccurs="0">  
                    <xs:unique name="AssessmentResultIterationMetricValuesUniqueProgrammaticName">  
                      <xs:selector xpath="MetricValue"/>  
                      <xs:field xpath="ProgrammaticName"/>  
                    </xs:unique>  
                  </xs:element>  
                  <xs:element name="MetricThresholds" type="MetricThresholds" minOccurs="0"/>  
                  <xs:element name="SolutionData" type="SolutionData" minOccurs="0"/>  
                  <xs:element name="Ordinal" type="xs:unsignedInt" minOccurs="0"/>  
                  <xs:element name="Trace" type="Trace" minOccurs="0"/>  
                  <xs:element name="Issues" type="Issues" minOccurs="0"/>  
                  <xs:element name="TestCases" minOccurs="0">  
                    <xs:complexType>  
                      <xs:sequence>  
                        <xs:element name="TestCase" maxOccurs="unbounded">  
                          <xs:complexType>  
                            <xs:all>  
                              <xs:element name="Key" type="xs:string"/>  
  
                              <xs:element name="ActivityReference" type="xs:string" minOccurs="0" />  
                              <xs:element name="Subject" minOccurs="0">  
                                <xs:complexType>  
                                  <xs:all>  
                                    <xs:element name="Class" type="DescriptionBasic" />  
                                    <xs:element name="Instance" type="DescriptionBasic" minOccurs="0"/>  
                                  </xs:all>  
                                </xs:complexType>  
                              </xs:element>  
  
                              <xs:element name="Name" type="xs:string" minOccurs="0"/>  
                              <xs:element name="ToolTip" type="xs:string" minOccurs="0"/>  
                              <xs:element name="Parents" minOccurs="0">  
                                <xs:complexType>  
                                  <xs:sequence>  
                                    <xs:element name="Parent" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>  
                                  </xs:sequence>  
                                </xs:complexType>  
                              </xs:element>  
                              <xs:element name="MetricValues" type="MetricValues" minOccurs="0">  
                                <xs:unique name="AssessmentResultIterationTestCaseMetricValuesUniqueProgrammaticName">  
                                  <xs:selector xpath="MetricValue"/>  
                                  <xs:field xpath="ProgrammaticName"/>  
                                </xs:unique>  
                              </xs:element>  
                              <xs:element name="MetricThresholds" type="MetricThresholds" minOccurs="0"/>  
                              <xs:element name="Issues" type="Issues" minOccurs="0"/>  
                            </xs:all>  
                          </xs:complexType>  
                        </xs:element>  
                      </xs:sequence>  
                    </xs:complexType>  
                  </xs:element>  
                </xs:all>  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="Traces" minOccurs="0">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="Trace" type="Trace" maxOccurs="unbounded"/>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="LocalizedStringDictionary" type="LocalizedStringDictionary" minOccurs="0"/>  
    </xs:all>  
    <xs:attribute name="SchemaVersion" type="xs:decimal" use="required" fixed="1.1"/>  
  </xs:complexType>  
  
    
  <xs:complexType name="AxeJobResults">  
    <xs:all>  
        
      <xs:element name="Id">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="Guid" type="Guid"/>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="MachineConfiguration">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="EcoSysInfo">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:any processContents="skip" minOccurs="0" maxOccurs="unbounded"/>  
                </xs:sequence>  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="Meta">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="JobStartDateTime" type="xs:dateTime"/>  
            <xs:element name="JobDuration" type="xs:unsignedLong"/>  
            <xs:element name="SessionLogFiles" type="xs:string" minOccurs="0"/>  
            <xs:element name="ExecutionGuid" type="Guid"/>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="AnalysisJobInfo">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="PlatformVersion" type="Version"/>  
            <xs:element name="Details">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="Start" type="xs:dateTime"/>  
                  <xs:element name="Duration" type="xs:unsignedLong"/>  
                  <xs:element name="SessionLogFiles" type="xs:string" minOccurs="0"/>  
                </xs:all>  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="ErrorsAndWarnings" type="ErrorsAndWarnings" minOccurs="0" />  
            <xs:element name="AnalysisJobAssessmentManifests">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="AxeAssessmentManifest" type="NestedVerificationScope" minOccurs="0" maxOccurs="unbounded"/>  
                </xs:sequence>  
              </xs:complexType>  
            </xs:element>  
          </xs:all>  
        </xs:complexType>  
      </xs:element>   
  
      <xs:element name="AxeJobManifest" type="NestedVerificationScope"/>  
  
      <xs:element name="AssessmentResults">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="ErrorsAndWarnings" type="ErrorsAndWarnings" minOccurs="0" />  
            <xs:element name="AssessmentResult" type="NestedVerificationScope" maxOccurs="unbounded"/>  
            <xs:element name="ErrorsAndWarnings" type="ErrorsAndWarnings" minOccurs="0" />  
          </xs:sequence>  
        </xs:complexType>  
      </xs:element>  
  
      <xs:element name="SolutionData" type="SolutionData" minOccurs="0"/>  
        
    </xs:all>  
    <xs:attribute name="SchemaVersion" type="xs:decimal" use="required" fixed="1.1"/>  
  </xs:complexType>  
  
</xs:schema>   
```



 

 




