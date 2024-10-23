# Created by anooppottammal at 10/21/24
Feature: Test for help page
scenario:user can select topic from help page
    Given open help page and returns
    When  verify help returns page opened
    Then  select Help topic Target Circle
    Then  verify Target Circle™ page opened

