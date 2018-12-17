#ifndef CMDPARSE_HPP
#define CMDPARSE_HPP

#include <algorithm> // For std::find
#include <string> // To use strings and length()
#include <iostream> // To use cout
#include <sstream> // To use string splitting
#include <vector> // To use vectors

class CMDParse {
   private:
      /* Variables */
      std::vector< std::string > args = {};
      std::vector< std::string > acceptedCommands = {};
      
      /* Functions */
      void parseArguments(unsigned int, char*[]);
      void parseCommands(std::string commands);
      std::vector<std::string> split(const std::string&, char);
      
   public:
      CMDParse(int, char*[], std::string);
      CMDParse();
      ~CMDParse();
      std::vector< std::string > getArguments() {
         return args;
      }
};

namespace cmdp {

   std::vector<std::string> parse(int argc,
                                  char* argv[], 
                                  std::string commands
                                 ) 
   {
      /*
       * Parses the commands given in argv, 
       * then returns these in a vector of strings.
       */
      CMDParse c = CMDParse(argc, argv, commands);
      return c.getArguments();
   }

}

#endif
