#!/usr/bin/env python
# coding: utf-8

# In[6]:


from transformers import pipeline

def generate_solidity_code(scenario, contract_type):
    """
    Uses Hugging Face's NLP model to generate Solidity smart contracts.
    """
    generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")

    # Predefined contract templates
    if contract_type == "ERC20 Token":
        return """
        // SPDX-License-Identifier: MIT
        pragma solidity ^0.8.0;

        contract Token {
            string public name = "Sample Token";
            string public symbol = "SMT";
            uint256 public totalSupply = 1000000;

            mapping(address => uint256) public balances;

            constructor() {
                balances[msg.sender] = totalSupply;
            }

            function transfer(address to, uint256 amount) public {
                require(balances[msg.sender] >= amount, "Not enough tokens");
                balances[msg.sender] -= amount;
                balances[to] += amount;
            }
        }
        """

    elif contract_type == "Voting System":
        return """
        // SPDX-License-Identifier: MIT
        pragma solidity ^0.8.0;

        contract Voting {
            struct Candidate {
                string name;
                uint256 votes;
            }

            Candidate[] public candidates;
            mapping(address => bool) public hasVoted;

            function addCandidate(string memory name) public {
                candidates.push(Candidate(name, 0));
            }

            function vote(uint256 candidateIndex) public {
                require(!hasVoted[msg.sender], "Already voted");
                candidates[candidateIndex].votes += 1;
                hasVoted[msg.sender] = true;
            }
        }
        """

    else:
        # Use NLP model for custom contracts
        response = generator(f"Generate a Solidity smart contract for: {scenario}", max_length=200, do_sample=True)
        return f"""
        // SPDX-License-Identifier: MIT
        pragma solidity ^0.8.0;

        // Auto-generated based on scenario: {scenario}
        contract CustomContract {{
            {response[0]["generated_text"]}
        }}
        """



# In[ ]:




