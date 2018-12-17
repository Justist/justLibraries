#include "cmdParse.hpp"

CMDParse::CMDParse(int argc, char* argv[], std::string commands) {
   parseCommands(commands);
   parseArguments(argc, argv);
}

CMDParse::CMDParse() {
   std::cout << R"(
Usage:
   It is highly preferable to use the cmdp::parse() command, 
   as defined in the header. This requires argc, argv, and a string
   of acceptable commands, comma-separated.
   Same goes for this class btw, so if you intend on using this class only,
   please give the same input and try again.
   )";
}

CMDParse::~CMDParse() {

}

void CMDParse::parseArguments(unsigned int argc, char* argv[]) {
   std::string arg = "";
   for(unsigned int i = 1; i < argc; i++) {
      arg = argv[i];
      if(std::find(acceptedCommands.begin(), 
                   acceptedCommands.end(),
                   arg) != acceptedCommands.end()) {
         args.push_back(argv[++i]);
      }
   }
}

void CMDParse::parseCommands(std::string commands) {
   for(std::string c : split(commands, ',')) {
      if(c.length() == 1) { acceptedCommands.push_back("-" + c); }
      else { acceptedCommands.push_back("--" + c); }
   }
}

std::vector<std::string> CMDParse::split(const std::string &s, char delim) {
   /*
    * Splits a string based on a certain delimiter and returns
    * the splitted elements in a vector.
    * Copied from https://stackoverflow.com/a/27511119/1762311
    */
   std::stringstream ss(s);
   std::string item;
   std::vector<std::string> elems;
   while (std::getline(ss, item, delim)) {
      //elems.push_back(item);
      elems.push_back(std::move(item));
   }
   return elems;
}
