/*

This smart contract is used to create new domain inside colony.
It is for colony address - 0x3E22fe63a6a920DBd6D0E0C7Af2BAA24a6a58289
Add this smart contract address as rootUser
Anyone can create their own Domain if msg.sender has more then 0.1 tokens
That sender becomes manager of newly created domainId
Later on, funds can be converted back to ETH

n number of tokens will be sent to newly created pot
tokens will flow from default to new pot

*/

pragma solidity ^0.4.23;
pragma experimental "v0.5.0";


//contains function signatures required to move fund
contract iColony {
    
    function addDomain(uint256 _parentSkillId) public;
    function moveFundsBetweenPots(uint256 _fromPot, uint256 _toPot, uint256 _amount, address _token) public;
    function getDomainCount() public view returns (uint256);
    function mintTokens(uint256 _wad) public;
    
}

contract EIP20Interface {
    
    function balanceOf(address _owner) public view returns (uint256 balance);
    function transfer(address _to, uint256 _value) public returns (bool success);
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success);
}

contract DomainCreator {
    
    address owner;
    address colony_address;
    address token_address;
    uint256 parentSkillId;
    uint256 MIN_WEI;
    
    constructor() public {
        
        owner = msg.sender;
        colony_address = 0x3E22fe63a6a920DBd6D0E0C7Af2BAA24a6a58289;
        token_address = 0x23551eC4Baf11C152b32c4606D52EfbDA0c45c3d;
        parentSkillId = 45;
        MIN_WEI = 100000000000000000;
        
    }
    
    function addDomain() payable public {
        
        //require(EIP20Interface(token_address).balanceOf(msg.sender)>=1000);
        
        require(msg.value>=MIN_WEI);
        
        iColony(colony_address).addDomain(parentSkillId);
        
        //iColony(colony_address).mintTokens(msg.value * 1000);
        
        iColony(colony_address).moveFundsBetweenPots(1, iColony(colony_address).getDomainCount(), (msg.value * 1000), token_address);
        
        owner.transfer(msg.value);

    }
    
    function claimEther(uint256 _amount) public {
        
        require(EIP20Interface(token_address).balanceOf(msg.sender) >= (MIN_WEI * 1000));
        
        EIP20Interface(token_address).transferFrom(msg.sender, token_address, _amount);
        
        address(msg.sender).transfer((_amount / 1000));
        
    }
    
}
