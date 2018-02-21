'''
Script Name  :  to_connect_system_using_paramiko.py            
Purpose      :  for making SSH2 connections (client or server) using python paramiko package  
Author       :  Arihant Jain                                  
Created Date :  21-Feb-2018
'''
import paramiko
import os
import sys
host = 'xyz.com'
username = "root";
password = "abc123";

def create_connection_ssh(host=host, username=username, password=password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            print "creating connection..."
            print "connected"
            print ""
            ssh.connect(host,username=username,password=password)
        except:
                print"something wrong"
        finally:
                print "closing connection..."
                ssh.close()
                print "closed"

if __name__ == '__main__':
    create_connection_ssh(host,username,password)
