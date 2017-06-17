"""
    Author: pablopg.
    Step-by-step:
        1. Run pip install boto3
        2. Run pip install --upgrade --user awscli (http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
        3. Add awscli to the path (http://docs.aws.amazon.com/cli/latest/userguide/awscli-install-windows.html#awscli-install-windows-path)
        4. Create an user in the AWS CLI.
        5. Configure local AWS cli via the command: aws configure --profile adminuser
        6. Run and listen!
"""

"""Getting Started Example for Python 2.7+/3.3+"""
import copilot

if __name__ == '__main__':
    # Create Copilot object.
    alicia = copilot.copilot_obj()

    # Start copilot.
    alicia.start()

    # While(1) loop.
    alicia.run()
